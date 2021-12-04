from PySide6.QtWidgets import QMainWindow

from NoteTableModel import NoteTableModel
from NoteApiProvider import NoteApiProvider

from Ui_MainWindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.__ui = Ui_MainWindow()
        self.__ui.setupUi(self)

        model = NoteTableModel(NoteApiProvider('http://localhost:8080'), self)
        self.__ui.tableView.setModel(model)

        model.update_model()
