from PySide6.QtCore import Slot, Qt, QAbstractTableModel, QModelIndex, QTimer

from NoteApiProvider import NoteApiProvider


class NoteTableModel(QAbstractTableModel):
    __update_timeout = 10_000
    __columns = ['author', 'message']

    def __init__(self, provider, parent=None):
        super().__init__(parent)
        self.__api: NoteApiProvider = provider
        self.__notes = []
        self.__timer = QTimer(self)

        self.__timer.timeout.connect(self.update_model)

        self.__timer.start(self.__update_timeout)
        self.update_model()

    def columnCount(self, parent=QModelIndex()) -> int:
        return len(self.__columns)

    def rowCount(self, parent=QModelIndex()) -> int:
        return len(self.__notes)

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            row, column = index.row(), index.column()

            if row < self.rowCount() and column < self.columnCount():
                return self.__get_display_data(row, column)

        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        return self.__columns[section] \
                if orientation == Qt.Horizontal and role == Qt.DisplayRole \
                else None

    def note(self, row):
        return self.__notes[row]

    @Slot()
    def update_model(self):
        notes = self.__api.get_notes()

        if notes != self.__notes:
            self.beginResetModel()
            self.__notes = notes
            self.endResetModel()

    def __get_display_data(self, row: int, column: int) -> str:
        return self.__notes[row][self.__columns[column]]
