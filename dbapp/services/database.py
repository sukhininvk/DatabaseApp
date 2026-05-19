import mysql.connector

class DBService:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def connect(self, host: str, user: str, password: str):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        self.cursor = self.connection.cursor()

    def disconnect(self):
        if self.connection:
            self.connection.close()

        self.connection = None
        self.cursor = None

    def get_databases(self):
        raise NotImplementedError

    def get_tables(self):
        raise NotImplementedError

    def fetch_all(self):
        raise NotImplementedError

    def sql_execute(self, query):
        raise NotImplementedError
