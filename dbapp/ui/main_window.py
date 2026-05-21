from PySide6.QtWidgets import QMainWindow, QMessageBox

from dbapp.ui.generated.main_window import Ui_MainWindow
from dbapp.ui.connection_dialog import ConnectionDialog

class MainWindow(QMainWindow):
    def __init__(self, db_service, crud_service):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.db_service = db_service

        self.ui.actionConnect.triggered.connect(self.open_connection_dialog)
        self.ui.actionDisconnect.triggered.connect(self.disconnect_from_server)

        self.connection_required_widgets = [
            self.ui.actionDisconnect,

            self.ui.listWidget,
            self.ui.tableWidget
        ]

    def update_ui_state(self):
        connected = self.db_service.connection is not None

        for widget in self.connection_required_widgets:
            widget.setEnabled(connected)

    def open_connection_dialog(self):
        dialog = ConnectionDialog(self.db_service, self)
        dialog.connected.connect(self.update_ui_state)
        dialog.connected.connect(self.load_tables)
        dialog.exec()

    def disconnect_from_server(self):
        self.db_service.disconnect()
        self.ui.listWidget.clear()
        self.update_ui_state()

    def load_tables(self):
        try:
            tables = self.db_service.get_tables()
        except Exception as err:
            QMessageBox.critical(self, "Error", str(err))
        else:
            self.ui.listWidget.clear()
            self.ui.listWidget.addItems(tables)
