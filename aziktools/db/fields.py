"""
    used to create a column part of sql when creating table using migrate.py
    for example "INSERT INTO table_name(<CharField>,<IntegerField>, ... )"
    <CharField> creates "VARCHAR(200) NOT NULL" and it will be put to the sql query
"""


class CharField:
    def __init__(self, max_length=200, null=False):
        self.max_length = max_length
        self.null = null

    def make_sql_field(self):
        if not self.null:
            sql = f"""VARCHAR({self.max_length}) NOT NULL"""
            return sql
        else:
            sql = f"""VARCHAR({self.max_length})"""
            return sql


class IntegerField:
    def __init__(self, null=False):
        self.null = null

    def make_sql_field(self):
        if not self.null:
            sql = f"""INT NOT NULL"""
            return sql
        else:
            sql = f"""INT"""
            return sql
