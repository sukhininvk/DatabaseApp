class CrudService:
    def __init__(self, db_service):
        self.db_service = db_service

    def select_table(self):
        raise NotImplementedError

    def insert_row(self, *args: str):
        raise NotImplementedError

    def update_row(self, *args: str):
        raise NotImplementedError

    def delete_row(self):
        raise NotImplementedError
