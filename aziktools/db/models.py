# importing main database connection
from aziktools.db.connection import db

from aziktools.db.fields import CharField, IntegerField
import app.my_models
import inspect

"""QuerySet is a list of models that are created by fetching data from database table"""


class QuerySet:
    def __init__(self, data, class_name, fields):
        # tuple list that are fetched from database table
        # for example [(1,'Susan', 'susan2005@gmail.com'),(2,'Smith', 'jsmith005@gmail.com')
        self.data = data

        # queryset should know the class name of table in order to create model instances
        # for example 'User', 'Category' etc.
        self.class_name = class_name

        # fields are Model attributes (table columns)
        # for example fields = ['id', 'name', 'surname', 'age', 'email'] etc.
        self.fields = fields

        # creating empty list to store model instances
        instances = []

        for row in data:
            # creating dictionary from fields and data
            # fields become dict keys and data row become dict values
            attrs = dict(zip(self.fields, row))

            # call class dynamically by it's name and pass **attrs to create object instance
            _object = getattr(app.my_models, self.class_name)(**attrs)

            # add instance to instances list
            instances.append(_object)

        # save instances list to an attribute to use it freely
        self.instances = instances


"""Objects is class that is used to make database operations. Every Model that is created by inheriting Model class 
will have a global attribute called objects. 
 Usage example: User.objects.all() returns a QuerySet """


class Objects:
    def __init__(self, table_name, class_name, fields):
        # table name is used to make any database operation
        self.table_name = table_name

        # class_name is used to create QuerySet
        self.class_name = class_name

        # fields is used to create QuerySet
        self.fields = fields

    # returns Queryset. this function fetches all data from a spesific table
    def all(self):
        # tuple list that are fetched from database table
        # for example [(1,'Susan', 'susan2005@gmail.com'),(2,'Smith', 'jsmith005@gmail.com')
        data = db.query(f"""SELECT * FROM {self.table_name}""")

        queryset = QuerySet(data, self.class_name, self.fields)
        return queryset

    def get(self, **kwargs):
        for key, value in kwargs.items():
            sql = f"""SELECT * FROM {self.table_name} WHERE {key}='{value}'"""
            return db.query(sql)

    # used to insert data into table in database. note that this function will not be used from user directly.
    def create(self, kwargs):
        sql = f"""INSERT INTO {self.table_name}("""
        for key in kwargs.keys():
            sql += f"""{key},"""
        sql = sql[:-1] + ") VALUES("
        for value in kwargs.values():
            sql += f"""'{value}',"""
        sql = sql[:-1] + ") RETURNING *"

        result = db.query(sql)
        db.connection.commit()
        return result


"""Base class to create Models. """


class Model:
    objects = None

    def __init__(self, **kwargs):
        # id is created automatically by database so we dont need to get id from user. at first it will be None
        self.id = None

        # initializing attributes values
        self.__dict__.update(kwargs)

        # # extracting all field names. id is common
        fields = ['id']

        # returns all "members" of a class including set of user defined attributes
        attrs = inspect.getmembers(self.__class__)
        model_attrs = attrs[2][1]

        # excluding built in attributes and collecting only user defined ones
        for attr in model_attrs:
            if '__' not in attr and attr != 'objects':
                fields.append(attr)

        self.fields = fields

        # any table in database will be created with the name "main_<class_name>". note that class name will be lowered
        self.table_name = "main_" + self.__class__.__name__.lower()

        # creating global "objects" attribute from Objects class for the derived model class.
        self.__class__.objects = Objects(self.table_name, self.__class__.__name__, self.fields)

    """ save() is
        used to insert row to database table.
        example:
        >>> user = User(name='Azizbek', surname='Xushnazarov') # insertion is not done yet.
        >>> user.save() # inserting starts and returns the Model instance if succeed
    """

    def save(self):
        # creating field:value dictionary
        model_data = {}
        for field in self.fields:
            if field != 'id':
                model_data[field] = getattr(self, field)

        # model instance will be created
        instance = self.__class__.objects.create(model_data)

        # id will be assigned to the instance
        self.id = instance[0]

        return instance
