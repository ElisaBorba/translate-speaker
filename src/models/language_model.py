from database.db import db
from .abstract_model import AbstractModel
from typing import Dict


class LanguageModel(AbstractModel):
    _collection = db["languages"]

    def __init__(self, data: Dict[str, str]):
        super().__init__(data)

    def to_dict(self):
        return {
            "name": self.data["name"],
            "acronym": self.data["acronym"],
        }
