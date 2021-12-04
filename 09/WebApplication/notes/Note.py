import uuid

from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class Note:
    id: uuid
    author: str
    message: str

    def to_json(self) -> Dict[str, Any]:
        return {
            'id': str(self.id),
            'author': self.author,
            'message': self.message,
        }
