from PySide6.QtWidgets import QMessageBox

class ConnectService:
    def __init__(self, db_service):
        self.db = db_service

    def connect_from_dialog(self, dialog):
        host = dialog.HostnameLineEdit.text()
        user = dialog.UsernameLineEdit.text()
        password = dialog.PassworgLineEdit.text()

        try:
            self.db.connect(host, user, password)
            return True

        except Exception as e:
            QMessageBox.critical(dialog, "Ошибка подключения", str(e))
            return False
