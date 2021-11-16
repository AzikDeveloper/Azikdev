import inspect

from db.connection import db
from db.fields import *


class Objects:
    def __init__(self, table_name):
        self.table_name = table_name

    def all(self):
        return db.query(f"""SELECT * FROM {self.table_name}""")

    def get(self, **kwargs):
        for key, value in kwargs.items():
            sql = f"""SELECT * FROM {self.table_name} WHERE {key}='{value}'"""
            return db.query(sql)

    def create(self, **kwargs):
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


class Model:
    objects = None

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self.fields = kwargs.keys()
        self.table_name = "main_" + self.__class__.__name__.lower()
        Model.objects = Objects(self.table_name)

    def save(self):
        model_data = {}
        for field in self.fields:
            model_data[field] = getattr(self, field)
        instance = Model.objects.create(**model_data)
        return instance
