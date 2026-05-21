import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon

from dbapp.ui.main_window import MainWindow
from dbapp.services.database import DBService
from dbapp.services.crud import CrudService

from dbapp.resources import resources  # noqa: F401

def main():
    app = QApplication(sys.argv)

    app.setWindowIcon(QIcon(":/icons/icon.png"))

    db_service = DBService()
    crud_service = CrudService(db_service)
    window = MainWindow(db_service, crud_service)

    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
