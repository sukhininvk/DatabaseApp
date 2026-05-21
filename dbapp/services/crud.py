class CrudService:
    def __init__(self, db_service):
        self.db_service = db_service

    def insert_row(self):
        raise NotImplementedError

    def update_row(self):
        raise NotImplementedError

    def delete_row(self):
        raise NotImplementedError