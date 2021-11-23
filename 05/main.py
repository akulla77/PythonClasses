from notes.Note import Note
from notes.NoteManager import NoteManager
from notes.Storage import ReadOnlyStorage, ReadWriteStorage


if __name__ == '__main__':
    main_storage = ReadWriteStorage('~/data')

    personal_notes_manager = NoteManager('personal', main_storage)
    personal_notes_manager.add_note(Note(0, 'user_1', 'note_1'))
    personal_notes_manager.add_note(Note(1, 'user_1', 'note_2'))
    print(personal_notes_manager.get_all_notes())

    work_notes_manager = NoteManager('work', main_storage)

    n = Note(2, 'user_2', '**')
    print(n.message)
    work_notes_manager.add_note(n)
    print(work_notes_manager.get_all_notes())

    # тесты
    tmp_storage = ReadOnlyStorage('/tmp/tests/data')
    tmp_storage.get_one(1)
