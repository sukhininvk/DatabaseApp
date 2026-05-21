class CrudService:
    def __init__(self, db_service):
        self.db_service = db_service

    def select_table(self, table_name):
        cursor = self.db_service.cursor()

        query = f"SELECT * FROM \"{table_name}\""
        self.db_service.sql_execute(query)

        rows = cursor.fetchall()
        headers = [description[0] for description in cursor.description]

        return headers, rows

    def insert_row(self):
        raise NotImplementedError

    def update_row(self):
        raise NotImplementedError

    def delete_row(self):
        raise NotImplementedError
