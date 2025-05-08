from aps.models.rest_item import RestItem
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String


class Pokemon(RestItem):
    __tablename__ = "pokemon"
    id : Mapped[int]= mapped_column(primary_key=True, autoincrement=True)
    name : Mapped[str]= mapped_column(unique=True)
    type : Mapped[str]= mapped_column(String(80), default="unknown")
    generation : Mapped[str]= mapped_column(String(80), default="unknown")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "type": self.type,
            "generation": self.generation
        }
