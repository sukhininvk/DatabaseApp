from dbapp.services import DBService, CrudService, SchemaService
from dbapp.controllers import ConnectionController, TreeViewController, TableWidgetController
from dbapp.ui import MainWindow, ConnectionDialog


class AppContainer:
    def __init__(self):
        self.db_service = DBService()
        self.crud_service = CrudService(self.db_service)
        self.schema_service = SchemaService(self.db_service)

        self.main_window = MainWindow()
        self.connection_dialog = ConnectionDialog()

        self.connection_controller = ConnectionController(
            self.db_service,
            self.main_window,
            self.connection_dialog
        )

        self.tree_view_controller = TreeViewController(
            self.schema_service,
            self.main_window,
            self.db_service
        )

        self.table_widget_controller = TableWidgetController(
            self.main_window,
            self.db_service,
            self.schema_service,
            self.crud_service
        )
