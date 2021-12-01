import json
import re

from commands import AbstractCommand

from notes.Note import Note
from notes.Storage import AbstractStorage


class PutNoteCommand(AbstractCommand):
    def __init__(self, storage: AbstractStorage):
        super().__init__(storage)

    @property
    def name(self) -> str:
        return 'PUT_NOTE'

    @property
    def help(self) -> str:
        return 'Inserts new note or updates existent.'

    @property
    def arguments(self) -> list:
        return ['data']

    def can_execute(self, command: str) -> bool:
        return re.match(rf'^{self.name} (.*)$', command) is not None

    def execute(self, options: dict):
        try:
            self._storage.put_one(Note(**json.loads(options['data'])))
        except (TypeError, ValueError) as error:
            print(f'ERROR: {error}')
