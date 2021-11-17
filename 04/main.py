from dataclasses import dataclass
from typing import Dict, Iterable


@dataclass
class Note:
    id: int
    author: str
    message: str


GLOBAL_NOTES: Dict[int, Note] = {}


def get_all_notes() -> Iterable[Note]:
    return GLOBAL_NOTES.values()


def add_note(note: Note):
    GLOBAL_NOTES[note.id] = note


def remove_note(note_id: int):
    del GLOBAL_NOTES[note_id]


if __name__ == '__main__':
    add_note(Note(0, 'user_1', 'note_1'))
    add_note(Note(1, 'user_1', 'note_2'))

    print(get_all_notes())

    remove_note(0)
    print(get_all_notes())
