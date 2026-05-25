class SchemaService:
    def __init__(self, db_service):
        self.db_service = db_service

    def get_databases(self) -> list[str]:
        query = "SHOW DATABASES"
        result = self.db_service.fetch_all(query)

        return [row[0] for row in result]

    def get_tables(self, database_name: str) -> list[str]:
        query = f"SHOW TABLES FROM `{database_name}`"
        result = self.db_service.fetch_all(query)

        return [row[0] for row in result]

    def get_schema(self) -> dict[str, list[str]]:
        schema = {}
        databases = self.get_databases()

        for database in databases:
            tables = self.get_tables(database)
            schema[database] = tables

        return schema