from PySide6.QtWidgets import QMainWindow

from dbapp.ui.generated.main_window import Ui_MainWindow
from dbapp.ui.connection_dialog import ConnectionDialog

class MainWindow(QMainWindow):
    def __init__(self, db_service, crud_service):
        super().__init__()

        self.db_service = db_service

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.connectButton.clicked.connect(self.open_connection_dialog)

        self.connection_required_widgets = [
            self.ui.refreshButton.clicked.connect(db_service.fetch_all),
            self.ui.insertRowButton.clicked.connect(crud_service.insert_row),
            self.ui.updateRowButton.clicked.connect(crud_service.update_row),
            self.ui.deleteRowButton.clicked.connect(crud_service.delete_row)
        ]

    def open_connection_dialog(self):
        dialog = ConnectionDialog(self.db_service, self)
        dialog.exec()

    def update_ui_state(self):
        connected = self.db_service.connection is not None

        for widget in self.connection_required_widgets:
            widget.setEnabled(connected)
