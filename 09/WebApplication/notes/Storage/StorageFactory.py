from notes.Storage import *


class StorageFactory(object):
    __storages = {
        'memory': MemoryStorage,
        'mongo': MongoStorage,
    }

    @classmethod
    def create_storage(cls, settings: dict) -> AbstractStorage:
        storage: AbstractStorage = cls.__storages[settings.get('storage', 'memory')]()

        if isinstance(storage, MongoStorage):
            storage.create(settings['connection'], settings['database'], settings['collection'])

        return storage
