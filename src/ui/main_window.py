from PySide6.QtWidgets import QMainWindow, QDialog

from services.query_editor import QueryEditorService
from ui.connection_dialog import ConnectionDialog
from ui.generated.main_window import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.query_editor = QueryEditorService()

        self.ui.SQLQueryButton.clicked.connect(self.query_editor.open)

    def open_connect_dialog(self):
        dialog = ConnectionDialog()

        if dialog.exec_():
            self.db_service.connect(dialog.HostnameLineEdit.text())