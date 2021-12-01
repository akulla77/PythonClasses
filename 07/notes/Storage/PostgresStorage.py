import asyncpg

from typing import AsyncIterable

from notes.Note import Note
from notes.Storage import AbstractStorage


class PostgresStorage(AbstractStorage):
    def __init__(self):
        self.__connection = None

    async def create(self, options: dict):
        self.__connection = await asyncpg.connect(**options)

        await self.__connection.execute(
            'CREATE TABLE IF NOT EXISTS notes (id int PRIMARY KEY, author text, message text)'
        )

    async def get_all(self) -> AsyncIterable[Note]:
        async with self.__connection.transaction():
            async for row in self.__connection.cursor('SELECT * FROM notes'):
                yield self.__make_note(row)

    async def get_one(self, key: int) -> Note | None:
        async with self.__connection.transaction():
            cursor = await self.__connection.cursor('SELECT * FROM notes WHERE id = $1', key)
            return self.__make_note(await cursor.fetchrow())

    async def put_one(self, note: Note):
        async with self.__connection.transaction():
            await self.__connection.execute(
                'INSERT INTO notes VALUES ($1, $2, $3) '
                '  ON CONFLICT (id) DO UPDATE SET id = $1, author = $2, message = $3',
                note.id, note.author, note.message
            )

    async def delete_one(self, key: int):
        async with self.__connection.transaction():
            await self.__connection.execute('DELETE FROM notes WHERE id = $1', key)

    @staticmethod
    def __make_note(row: tuple) -> Note | None:
        return Note(row[0], row[1], row[2]) if row else None
