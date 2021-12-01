from notes.Storage import *


class StorageFactory(object):
    __storages = {
        'memory': MemoryStorage,
        'mongo': MongoStorage,
        'postgres': PostgresStorage,
    }

    @classmethod
    async def create_storage(cls, settings: dict) -> AbstractStorage:
        storage: AbstractStorage = cls.__storages[settings.get('storage', 'memory')]()

        if isinstance(storage, MongoStorage):
            await storage.create(settings['connection'], settings['database'], settings['collection'])
        elif isinstance(storage, PostgresStorage):
            await storage.create(settings['connection'])

        return storage
