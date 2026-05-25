import mysql.connector
from mysql.connector.cursor import MySQLCursor


class DBService:
    def __init__(self):
        self.connection = None

    def connect(self, host: str, user: str, password: str):
        if self.is_connected():
            self.disconnect()

        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )

    def disconnect(self):
        if self.is_connected():
            self.connection.close()

        self.connection = None

    def is_connected(self) -> bool:
        return self.connection is not None

    def sql_execute(self, query: str, params=None) -> MySQLCursor | None:
        if self.is_connected():
            cursor = self.connection.cursor()
            cursor.execute(query, params)

            return cursor
        else:
            return None

    def fetch_all(self, query: str, params=None):
        cursor = self.sql_execute(query, params)

        if cursor is None:
            return []

        return cursor.fetchall()
