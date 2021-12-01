import re

from commands import AbstractCommand
from notes.Storage import AbstractStorage


class DeleteNoteCommand(AbstractCommand):
    def __init__(self, storage: AbstractStorage):
        super().__init__(storage)

    @property
    def name(self) -> str:
        return 'DELETE_NOTE'

    @property
    def help(self) -> str:
        return 'Deletes note.'

    @property
    def arguments(self) -> list:
        return ['node_id']

    def can_execute(self, command: str) -> bool:
        return re.match(rf'^{self.name} (\d+)$', command) is not None

    def execute(self, options: dict):
        try:
            self._storage.delete_one(int(options['node_id']))
        except ValueError as error:
            print(f'ERROR: {error}')
