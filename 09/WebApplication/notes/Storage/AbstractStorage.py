from abc import abstractmethod
from typing import AsyncIterable

from notes.Note import Note


class AbstractStorage(object):
    def create(self, *args, **kwargs):
        pass

    async def contains(self, key: str) -> bool:
        return await self.get_one(key) is not None

    @abstractmethod
    def get_all(self) -> AsyncIterable[Note]:
        raise NotImplementedError

    @abstractmethod
    async def get_one(self, key: str) -> Note:
        raise NotImplementedError

    @abstractmethod
    async def put_one(self, note: Note):
        raise NotImplementedError

    @abstractmethod
    async def delete_one(self, key: str):
        raise NotImplementedError
