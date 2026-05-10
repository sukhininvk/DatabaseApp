from ui.query_editor_window import QueryEditorWindow

class QueryEditorService:
    def __init__(self):
        self.window = None

    def open(self):
        if self.window is None:
            self.window = QueryEditorWindow()

        self.window.show()
        self.window.raise_()
        self.window.activateWindow()

    def close(self):
        if self.window:
            self.window.close()
            self.window = None
