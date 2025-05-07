from aps.models.rest_item import RestItem
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String


class Pokemon(RestItem):
    __tablename__ = "pokemon"
    id : Mapped[int]= mapped_column(primary_key=True, auto_increment=True)
    name : Mapped[str]= mapped_column(unique=True)
    type : Mapped[str]= mapped_column()
    generation : Mapped[str]= mapped_column(String(80))

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "type": self.type,
            "generation": self.generation
        }
