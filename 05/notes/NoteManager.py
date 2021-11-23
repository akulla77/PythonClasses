from typing import Iterable

from notes.Note import Note
from notes.Storage import AbstractStorage


class NoteManager:
    """
    Менеждер заметок. Управляет заметками определённой группы.
    """
    def __init__(self, name: str, storage: AbstractStorage):
        self.__name = name
        self.__storage = storage

    def get_all_notes(self) -> Iterable[Note]:
        return self.__storage.get_all()

    def add_note(self, note: Note):
        self.__storage.put_one(note)

    def remove_note(self, note_id: int):
        self.__storage.delete_one(note_id)
