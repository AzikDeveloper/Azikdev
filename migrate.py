import inspect
from app import my_models
from db.db import DB

db = DB()
for name, CLASS in inspect.getmembers(my_models):
    if inspect.isclass(CLASS):
        if 'my_models' in str(CLASS):
            model = CLASS()
            table_name = 'main_' + type(model).__name__.lower()
            # print(table_name)
            sql = f"""CREATE TABLE \"{table_name}\"(id serial PRIMARY KEY"""
            attrs = inspect.getmembers(CLASS)
            model_attrs = attrs[2][1]
            for i in model_attrs:
                if '__' not in i:
                    # print(i)
                    attr = getattr(model, i)
                    sql += f""", {i} {attr.make_sql_field()}"""
            sql += ")"

            existing_table_deletion_sql = f"""DROP TABLE IF EXISTS {table_name} """
            db.cursor.execute(existing_table_deletion_sql)
            db.connection.commit()

            db.cursor.execute(sql)
            db.connection.commit()
            # print(sql)
