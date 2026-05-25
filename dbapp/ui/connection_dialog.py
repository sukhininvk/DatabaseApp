from PySide6.QtWidgets import QDialog
from dbapp.ui.generated import Ui_ConnectionDialog


class ConnectionDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_ConnectionDialog()
        self.ui.setupUi(self)

        self.ui.cancelButton.clicked.connect(self.reject)

    def clear_fields(self):
        self.ui.hostnameLineEdit.clear()
        self.ui.usernameLineEdit.clear()
        self.ui.passwordLineEdit.clear()
