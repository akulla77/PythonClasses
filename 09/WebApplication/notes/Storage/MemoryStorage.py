from typing import AsyncIterable, Dict, Optional

from notes.Note import Note
from notes.Storage import AbstractStorage


class MemoryStorage(AbstractStorage):
    def __init__(self):
        self.__storage: Dict[str, Note] = {}

    async def contains(self, key: str) -> bool:
        return key in self.__storage

    async def get_all(self) -> AsyncIterable[Note]:
        for value in self.__storage.values():
            yield value

    async def get_one(self, key: str) -> Optional[Note]:
        return self.__storage.get(key)

    async def put_one(self, note: Note):
        self.__storage[str(note.id)] = note

    async def delete_one(self, key: str):
        if key in self.__storage:
            self.__storage.pop(key)
