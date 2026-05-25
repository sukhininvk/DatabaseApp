from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6.QtWidgets import QHeaderView
from PySide6.QtGui import QCloseEvent
from dbapp.ui.generated import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.splitter.setSizes([250, 800])
        self.ui.splitter.setStretchFactor(0, 0)
        self.ui.splitter.setStretchFactor(1, 1)

        self.connection_required_widgets = [
            self.ui.actionFetchSchemas,
            self.ui.actionDisconnect,
            self.ui.treeWidget,
            self.ui.tableWidget
        ]

        header = self.ui.treeWidget.header()

        header.setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionsMovable(False)
        header.setSectionsClickable(False)

    def closeEvent(self, event: QCloseEvent):
        reply = QMessageBox.question(
            self,
            "Confirm Exit",
            "Are you sure you want to exit?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No,
        )

        if reply == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()
