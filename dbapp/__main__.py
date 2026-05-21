import sys

from PySide6.QtWidgets import QApplication

from dbapp.ui.main_window import MainWindow
from dbapp.services.database import DBService
from dbapp.services.crud import CrudService
from dbapp.services.table import TableService

def main():
    app = QApplication(sys.argv)

    db_service = DBService()
    crud_service = CrudService(db_service)
    table_service = TableService(db_service)
    window = MainWindow(db_service,table_service, crud_service)

    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
