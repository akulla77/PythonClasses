import uuid

from typing import AsyncIterable, Optional

from motor.motor_asyncio import AsyncIOMotorClient

from notes.Note import Note
from notes.Storage import AbstractStorage


class MongoStorage(AbstractStorage):
    def __init__(self):
        self.__client = None
        self.__collection = None

    def create(self, connection: dict, database: str, collection: str):
        self.__client = AsyncIOMotorClient(self.__mongo_uri(**connection))
        self.__collection = self.__client[database][collection]

    async def get_all(self) -> AsyncIterable[Note]:
        async for value in self.__collection.find():
            yield self.__make_note(value)

    async def get_one(self, key: str) -> Optional[Note]:
        return self.__make_note(await self.__collection.find_one({'_id': key}))

    async def put_one(self, note: Note):
        value = note.to_json()
        value['_id'] = value.pop('id')
        await self.__collection.find_one_and_replace({'_id': str(note.id)}, value, upsert=True)

    async def delete_one(self, key: str):
        await self.__collection.delete_one({'_id': key})

    @staticmethod
    def __mongo_uri(host: str, port: int, user: str, password: str):
        return f'mongodb://{user}:{password}@{host}:{port}'

    @staticmethod
    def __make_note(value: dict) -> Optional[Note]:
        if value:
            value['id'] = uuid.UUID(value.pop('_id'))
            return Note(**value)

        return None
