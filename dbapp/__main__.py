import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from dbapp.core import AppContainer
from dbapp.resources import resources # noqa: F401

def main():
    app = QApplication(sys.argv)

    app.setWindowIcon(QIcon(":/icons/app_icon.png"))

    container = AppContainer()
    container.main_window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
