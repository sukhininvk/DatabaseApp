from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtCore import Signal

from dbapp.ui.generated.connection_dialog import Ui_ConnectionDialog

class ConnectionDialog(QDialog):
    connected = Signal()

    def __init__(self, db_service, parent=None):
        super().__init__(parent)

        self.ui = Ui_ConnectionDialog()
        self.ui.setupUi(self)

        self.db_service = db_service

        self.ui.cancelButton.clicked.connect(self.reject)
        self.ui.connectButton.clicked.connect(self.connect_to_server)

    def connect_to_server(self):
        try:
            self.db_service.connect(
                self.ui.hostnameLineEdit.text(),
                self.ui.usernameLineEdit.text(),
                self.ui.passwordLineEdit.text(),
                self.ui.databaseLineEdit.text()
            )
        except Exception as err:
            QMessageBox.critical(self, "Error", str(err))
        finally:
            self.connected.emit()
            self.close()
