from PySide6.QtWidgets import QTreeWidgetItem
from PySide6.QtGui import QIcon


class SchemaController:
    def __init__(self, schema_service, main_window, db_service):
        self.schema_service = schema_service
        self.main_window = main_window
        self.db_service = db_service
        self.treeWidget = self.main_window.ui.treeWidget

    def fetch_schemas(self):
        self.treeWidget.clear()
        self.treeWidget.setHeaderLabels(["Schemas"])
        self.treeWidget.setHeaderHidden(False)

        schema = self.schema_service.get_schema()

        for database_name, tables in schema.items():
            database_item = QTreeWidgetItem([database_name])
            database_item.setIcon(0, QIcon(":/icons/db_icon.png"))

            self.treeWidget.addTopLevelItem(database_item)

            for table_name in tables:
                table_item = QTreeWidgetItem([table_name])
                table_item.setIcon(0, QIcon(":/icons/table_icon.png"))

                database_item.addChild(table_item)

    def clear_tree_widget(self):
        self.treeWidget.clear()
        self.treeWidget.setHeaderHidden(True)
