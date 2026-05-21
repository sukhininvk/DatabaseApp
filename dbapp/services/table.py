class TableService:
    def __init__(self, db_service):
        self.db_service = db_service

    def get_tables(self) -> list[str]:
        if self.db_service.is_connected():
            cursor = self.db_service.sql_execute("SHOW TABLES")

            tables = [row[0] for row in cursor.fetchall()]
            cursor.close()

            return tables
        else:
            return []

    def fetch_table(self, table_name: str) -> tuple[list[str], list[tuple]]:
        query = f"SELECT * FROM `{table_name}` LIMIT 1000"

        cursor = self.db_service.sql_execute(query)

        rows = cursor.fetchall()
        headers = [
            description[0]
            for description in cursor.description
        ]

        cursor.close()

        return headers, rows
