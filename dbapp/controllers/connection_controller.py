from PySide6.QtWidgets import QMessageBox
from dbapp.ui.connection_dialog import ConnectionDialog


class ConnectionController:
    def __init__(self, db_service, main_window, schema_controller):
        self.db_service = db_service
        self.main_window = main_window
        self.schema_controller = schema_controller

        self._connect_signals()

    def _connect_signals(self):
        self.main_window.ui.actionConnect.triggered.connect(self.open_connection_dialog)
        self.main_window.ui.actionFetchSchemas.triggered.connect(self.schema_controller.fetch_schemas)
        self.main_window.ui.actionDisconnect.triggered.connect(self.disconnect_from_server)

    def open_connection_dialog(self):
        dialog = ConnectionDialog()
        dialog.ui.connectButton.clicked.connect(lambda: self.connect_to_server(dialog))
        dialog.exec()

    def connect_to_server(self, dialog):
        try:
            self.db_service.connect(
                dialog.ui.hostnameLineEdit.text(),
                dialog.ui.usernameLineEdit.text(),
                dialog.ui.passwordLineEdit.text()
            )
            self.schema_controller.fetch_schemas()
        except Exception as err:
            QMessageBox.critical(dialog, "Error", str(err))
        else:
            self.update_ui_state()
            dialog.accept()

    def update_ui_state(self):
        for widget in self.main_window.connection_required_widgets:
            widget.setEnabled(self.db_service.is_connected())

    def disconnect_from_server(self):
        self.db_service.disconnect()
        self.schema_controller.clear_tree_widget()
        self.update_ui_state()
