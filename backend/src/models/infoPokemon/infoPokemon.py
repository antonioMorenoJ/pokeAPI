from aps.models.rest_item import RestItem
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String


class InfoPokemon(RestItem):
    __tablename__ = "infoPokemon"
    __table_args__ = {'extend_existing': True}

    id : Mapped[int] = mapped_column(Integer, primary_key=True)
    pokemon_name : Mapped[str] = mapped_column(String(80), ForeignKey("pokemon.name"))
    move : Mapped[str] = mapped_column(String(80))
