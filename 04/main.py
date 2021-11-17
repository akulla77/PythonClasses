from dataclasses import dataclass
from typing import List


@dataclass
class Note:
    author: str
    message: str


GLOBAL_NOTES = []


def get_all_notes() -> List[Note]:
    return GLOBAL_NOTES


def add_note(note: Note):
    GLOBAL_NOTES.append(note)


def remove_note(index: int):
    GLOBAL_NOTES.pop(index)


if __name__ == '__main__':
    pass
