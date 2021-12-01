import sqlite3

from typing import Iterable


class SqliteDataStorage(object):
    def __init__(self, collection: str):
        self.__connection = sqlite3.connect(f'{collection}.db')
        self.__cursor = self.__connection.cursor()

    def get_objects(self) -> Iterable[dict]:
        self.__cursor.execute('SELECT * FROM objects')

        for row in self.__cursor:
            yield self.__extract_object(row)

    def get_object(self, key: str) -> dict:
        self.__cursor.execute('SELECT * FROM objects WHERE key = :key', {'key', key})
        return self.__extract_object(self.__cursor.fetchone())

    def get_any_object(self) -> dict:
        self.__cursor.execute('SELECT * FROM objects ORDER BY RANDOM() LIMIT 1')
        return self.__extract_object(self.__cursor.fetchone())

    @staticmethod
    def __extract_object(row: tuple) -> dict:
        return {
            'original': row[0],
            'translation': row[1],
            'transcription': row[2],
        } if row else None
