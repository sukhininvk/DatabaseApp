from dbapp.services import DBService, CrudService, SchemaService
from dbapp.controllers import ConnectionController, SchemaController, TableWidgetController
from dbapp.ui import MainWindow


class AppContainer:
    def __init__(self):
        self.db_service = DBService()
        self.crud_service = CrudService(self.db_service)
        self.schema_service = SchemaService(self.db_service)

        self.main_window = MainWindow()

        self.schema_controller = SchemaController(
            self.schema_service,
            self.main_window,
            self.db_service
        )

        self.connection_controller = ConnectionController(
            self.db_service,
            self.main_window,
            self.schema_controller
        )

        self.table_widget_controller = TableWidgetController(
            self.main_window,
            self.db_service,
            self.schema_service,
            self.crud_service
        )
