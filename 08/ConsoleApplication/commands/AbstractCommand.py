from abc import abstractmethod

from notes.Storage import AbstractStorage


class AbstractCommand(object):
    def __init__(self, storage: AbstractStorage):
        self._storage = storage

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def help(self) -> str:
        pass

    @property
    @abstractmethod
    def arguments(self) -> list:
        pass

    @abstractmethod
    def execute(self, options: dict):
        pass
