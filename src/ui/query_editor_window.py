from PySide6.QtWidgets import QMainWindow
from ui.generated.query_editor_window import Ui_QueryEditorWindow

class QueryEditorWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_QueryEditorWindow()
        self.ui.setupUi(self)
