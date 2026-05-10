from PySide6.QtWidgets import QDialog, QPushButton
from ui.generated.connecrion_dialog import Ui_ConnectionDialog
from services.db_service import DBService

class ConnectionDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.ui = Ui_ConnectionDialog()
        self.ui.setupUi(self)

        self.ui.ConnectButton.clicked.connect(self.connect)
        self.ui.CancelButton.clicked.connect(self.reject)
