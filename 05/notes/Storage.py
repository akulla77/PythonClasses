from abc import abstractmethod
from typing import Iterable

from notes.Note import Note


class AbstractStorage(object):
    """
    Определяет интерфейс хранилища заметок.
    """
    @abstractmethod
    def get_all(self) -> Iterable[Note]:
        raise NotImplemented

    @abstractmethod
    def get_one(self, note_id) -> Note | None:
        raise NotImplemented

    @abstractmethod
    def put_one(self, note: Note):
        raise NotImplemented

    @abstractmethod
    def delete_one(self, note_id: int):
        raise NotImplemented


class BaseStorage(object):
    """
    Базовый класс хранилища заметок (содержит только данные).
    """
    def __init__(self, folder: str):
        self._notes = {}
        self.__folder = folder


class ReadOnlyStorage(BaseStorage):
    """
    Хранилище заметок с возможностью только читать (добавляет методы выгрузки данных).
    """
    def get_all(self) -> Iterable[Note]:
        return self._notes.values()

    def get_one(self, note_id) -> Note | None:
        return self._notes.get(note_id)


class WriteOnlyStorage(BaseStorage):
    """
    Хранилище заметок с возможностью только (добавляет методы рекдатирования данных).
    """
    def put_one(self, note: Note):
        self._notes[note.id] = note

    def delete_one(self, note_id: int):
        del self._notes[note_id]


class ReadWriteStorage(ReadOnlyStorage, WriteOnlyStorage, AbstractStorage):
    """
    Хранилище заметок в оперативной памяти.
    """
    pass


class FileStorage(AbstractStorage):
    """
    Здесь может быть реализация хранилища в файле.
    """
    def __init__(self, filename: str):
        self.__filename = filename

    def get_all(self) -> Iterable[Note]:
        pass

    def get_one(self, note_id) -> Note | None:
        pass

    def put_one(self, note: Note):
        pass

    def delete_one(self, note_id: int):
        pass


class DatabaseStorage(AbstractStorage):
    """
    Здесь может быть реализация хранилища в базе данных.
    """
    def __init__(self, db_connection: str):
        self.__db_connection = db_connection

    def get_all(self) -> Iterable[Note]:
        pass

    def get_one(self, note_id) -> Note | None:
        pass

    def put_one(self, note: Note):
        pass

    def delete_one(self, note_id: int):
        pass
