from dataclasses import dataclass


@dataclass
class Note:
    id: int
    author: str
    message: str
