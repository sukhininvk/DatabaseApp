import mysql.connector

class DBService:
    def __init__(self):
        self.connection = None

    def connect(self, host: str, user: str, password: str, database: str):
        if self.is_connected():
            self.disconnect()

        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

    def disconnect(self):
        if self.is_connected():
            self.connection.close()

        self.connection = None

    def is_connected(self):
        return self.connection and self.connection.is_connected()

    def get_tables(self) -> list[str]:
        cursor = self.sql_execute("SHOW TABLES")

        tables = [table[0] for table in cursor.fetchall()]

        cursor.close()

        return tables

    def sql_execute(self, query: str, params=None):
        cursor = self.connection.cursor()
        cursor.execute(query, params)

        return cursor