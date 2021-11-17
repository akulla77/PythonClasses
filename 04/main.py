class Note:
    def __init__(self, note_id: int, author: str, message: str):
        self.__data = {
            'id': note_id,
            'author': author,
            'message': message,
        }

    @property
    def id(self) -> int:
        return self.__data['id']

    @property
    def message(self) -> str:
        return self.__data['message']

    @message.setter
    def message(self, message: str):
        self.__data['message'] = message

    @staticmethod
    def get_all_notes():
        return GLOBAL_NOTES.values()

    @staticmethod
    def add_note(note):
        GLOBAL_NOTES[note.id] = note

    @staticmethod
    def remove_note(note_id):
        del GLOBAL_NOTES[note_id]


GLOBAL_NOTES = {}


if __name__ == '__main__':
    Note.add_note(Note(0, 'user_1', 'note_1'))
    Note.add_note(Note(1, 'user_1', 'note_2'))

    note = Note(2, 'user_2', '**')
    print(Note.get_all_notes())

    Note.remove_note(0)
    print(Note.get_all_notes())
