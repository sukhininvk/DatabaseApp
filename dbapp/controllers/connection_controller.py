from PySide6.QtWidgets import QMessageBox


class ConnectionController:
    def __init__(self, db_service, main_window, connection_dialog):
        self.db_service = db_service
        self.main_window = main_window
        self.connection_dialog = connection_dialog

        self._connect_signals()

    def _connect_signals(self):
        self.main_window.ui.actionConnect.triggered.connect(self.open_connection_dialog)
        self.main_window.ui.actionDisconnect.triggered.connect(self.disconnect_from_server)
        self.connection_dialog.ui.connectButton.clicked.connect(self.connect_to_server)

    def open_connection_dialog(self):
        self.connection_dialog.clear_fields()
        self.connection_dialog.exec()

    def connect_to_server(self):
        try:
            self.db_service.connect(
                self.connection_dialog.ui.hostnameLineEdit.text(),
                self.connection_dialog.ui.usernameLineEdit.text(),
                self.connection_dialog.ui.passwordLineEdit.text()
            )
        except Exception as err:
            QMessageBox.critical(self.connection_dialog, "Error", str(err))
        else:
            self.update_ui_state()
            self.connection_dialog.close()

    def update_ui_state(self):
        for widget in self.main_window.connection_required_widgets:
            widget.setEnabled(self.db_service.is_connected())

    def disconnect_from_server(self):
        self.db_service.disconnect()
        self.main_window.ui.tableWidget.clear()
        self.update_ui_state()
