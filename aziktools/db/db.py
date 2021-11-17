import psycopg2

# importing databases from settings
from conf.settings import DATABASES

# use_db indicates which one to use from DATABASES
from conf.settings import use_db


class DB:

    def __init__(self):
        # creating connection
        self.connection = self.connect()

        # creating cursor from connection
        self.cursor = self.connection.cursor()

    # query is used to execute raw sql command and return spesific rows
    def query(self, sql: dict):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    @staticmethod
    def connect():
        print(f'Connecting to {use_db} ...')
        with psycopg2.connect(**DATABASES[use_db]) as connection:
            print(f'connected...')
            return connection

    # used to close database connection manually (not recommended)
    def close(self):
        self.connection.close()
