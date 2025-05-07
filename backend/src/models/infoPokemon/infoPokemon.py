from aps.models.rest_item import RestItem
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.testing.schema import mapped_column


class InfoPokemon(RestItem):
    __tablename__ = "infoPokemon"
    id : Mapped[int] = mapped_column(Integer, primary_key=True)
    pokemon_name : Mapped[str] = mapped_column(String(80), ForeignKey("infoPokemon.name"))
    move : Mapped[str] = mapped_column(String(80))

