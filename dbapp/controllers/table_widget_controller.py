from PySide6.QtWidgets import QMessageBox, QTableWidgetItem


class TableWidgetController:
    def __init__(self, main_window, db_service, schema_service, crud_service):
        self.main_window = main_window
        self.db_service = db_service
        self.schema_service = schema_service
        self.crud_service = crud_service

    def on_table_selected(self, item):
        table_name = item.text()

        try:
            columns, rows = self.schema_service.fetch_table(table_name)
        except Exception as err:
            QMessageBox.critical(self.main_window, "Error", str(err))
            return

        self.fill_table_widget(columns, rows)

    def fill_table_widget(self, columns, rows):
        table = self.main_window.tableWidget

        table.setUpdatesEnabled(False)

        self.clear_table_widget()

        table.setColumnCount(len(columns))
        table.setHorizontalHeaderLabels(columns)
        table.setRowCount(len(rows))

        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                table.setItem(i, j, QTableWidgetItem(str(value)))

        table.setUpdatesEnabled(True)

    def clear_table_widget(self):
        self.main_window.tableWidget.clear()
        self.main_window.tableWidget.setRowCount(0)
        self.main_window.tableWidget.setColumnCount(0)
