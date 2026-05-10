import mysql.connector

class DBService:
    def __init__(self):
        self.connection = None
        self.cursor = None
        self.current_database = None

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
        self.current_database = None

    def get_databases(self):
        self.cursor.execute("SHOW DATABASES")
        return [db[0] for db in self.cursor.fetchall()]

    def use_database(self, database_name: str):
        self.cursor.execute(f"USE {database_name}")
        self.current_database = database_name

    def get_tables(self):
        if not self.current_database:
            return []
        self.cursor.execute("SHOW TABLES")
        return [t[0] for t in self.cursor.fetchall()]

    def execute_query(self, query: str):
        if not self.cursor:
            raise Exception("Нет подключения к базе данных")

        self.cursor.execute(query)

        if self.cursor.with_rows:
            return self.cursor.fetchall()

        self.connection.commit()
        return None
