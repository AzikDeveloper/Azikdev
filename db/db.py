import psycopg2
from conf.settings import DATABASES
from conf.settings import use_db


class DB:

    def __init__(self):
        self.connection = self.connect()
        self.cursor = self.connection.cursor()

    def query(self, sql: dict):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    @staticmethod
    def connect():
        print(f'Connecting to {use_db} ...')
        with psycopg2.connect(**DATABASES[use_db]) as connection:
            print(f'connected...')
            return connection

    def close(self):
        self.connection.close()
