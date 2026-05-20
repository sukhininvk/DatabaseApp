from PySide6.QtWidgets import QMainWindow

from dbapp.ui.generated.main_window import Ui_MainWindow
from dbapp.ui.connection_dialog import ConnectionDialog

class MainWindow(QMainWindow):
    def __init__(self, db_service, crud_service):
        super().__init__()

        self.db_service = db_service

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.actionConnect.triggered.connect(self.open_connection_dialog)

        self.connection_required_widgets = [
            self.ui.actionFetch.triggered.connect(db_service.fetch_all),
            self.ui.actionDisconnect.triggered.connect(db_service.disconnect),

            self.ui.treeView,
            self.ui.tableWidget
        ]

    def open_connection_dialog(self):
        dialog = ConnectionDialog(self.db_service, self)
        dialog.exec()

    def update_ui_state(self):
        connected = self.db_service.connection is not None

        for widget in self.connection_required_widgets:
            widget.setEnabled(connected)
