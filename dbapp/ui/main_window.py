from PySide6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem

from dbapp.ui.generated.main_window import Ui_MainWindow
from dbapp.ui.connection_dialog import ConnectionDialog

class MainWindow(QMainWindow):
    def __init__(self, db_service, table_service, crud_service):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.db_service = db_service
        self.table_service = table_service
        self.crud_service = crud_service

        self.ui.actionConnect.triggered.connect(self.open_connection_dialog)
        self.ui.actionDisconnect.triggered.connect(self.disconnect_from_server)

        self.ui.listWidget.itemClicked.connect(self.on_table_selected)

        self.connection_required_widgets = [
            self.ui.actionDisconnect,

            self.ui.listWidget,
            self.ui.tableWidget
        ]

    def update_ui_state(self):
        connected = self.db_service.connection is not None

        for widget in self.connection_required_widgets:
            widget.setEnabled(connected)

    def open_connection_dialog(self):
        dialog = ConnectionDialog(self.db_service, self)
        dialog.connected.connect(self.update_ui_state)
        dialog.connected.connect(self.load_tables)
        dialog.exec()

    def disconnect_from_server(self):
        self.db_service.disconnect()
        self.ui.listWidget.clear()
        self.ui.tableWidget.clear()
        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.setColumnCount(0)
        self.update_ui_state()

    def load_tables(self):
        try:
            tables = self.table_service.get_tables()
        except Exception as err:
            QMessageBox.critical(self, "Error", str(err))
        else:
            self.ui.listWidget.clear()
            self.ui.listWidget.addItems(tables)

    def on_table_selected(self, item):
        table_name = item.text()

        columns, rows = self.table_service.fetch_table(table_name)
        self.fill_table_widget(columns, rows)

    def fill_table_widget(self, columns, rows):
        table = self.ui.tableWidget

        table.clear()

        table.setColumnCount(len(columns))
        table.setHorizontalHeaderLabels(columns)
        table.setRowCount(len(rows))

        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                table.setItem(i, j, QTableWidgetItem(str(value)))