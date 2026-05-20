from PySide6.QtWidgets import QDialog

from dbapp.ui.generated.connecrion_dialog import Ui_ConnectionDialog

class ConnectionDialog(QDialog):
    def __init__(self, db_service, parent=None):
        super().__init__(parent)

        self.ui = Ui_ConnectionDialog()
        self.ui.setupUi(self)

        self.db_service = db_service

        self.ui.CancelButton.clicked.connect(self.reject)
        self.ui.ConnectButton.clicked.connect(self.connect_db)

    def connect_db(self):
        self.db_service.connect(
            self.ui.HostnameLineEdit.text(),
            self.ui.UsernameLineEdit.text(),
            self.ui.PasswordLineEdit.text()
        )

        self.close()
