import re

from commands import AbstractCommand
from notes.Storage import AbstractStorage


class GetNoteCommand(AbstractCommand):
    def __init__(self, storage: AbstractStorage):
        super().__init__(storage)

    @property
    def name(self) -> str:
        return 'GET_NOTE'

    @property
    def help(self) -> str:
        return 'Prints note.'

    @property
    def arguments(self) -> list:
        return ['node_id']

    def can_execute(self, command: str) -> bool:
        return re.match(rf'^{self.name} (\d+)$', command) is not None

    def execute(self, options: dict):
        try:
            note_id = int(options['node_id'])

            if note := self._storage.get_one(note_id):
                print(note)
            else:
                print(f'ERROR: note "{note_id}" not found.')
        except ValueError as error:
            print(f'ERROR: {error}')
