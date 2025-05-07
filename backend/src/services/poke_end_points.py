from flask_smorest import Blueprint
from backend.src.models.pokemon.pokemon_schema import PokemonSchema
from backend.src.services.poke_service import get_or_fetch_pokemon_by_name

poke_blp = Blueprint("pokemon", "pokemon", url_prefix="/pokemon", description="Operaciones con Pokémon")

@poke_blp.route("/<string:name>")
@poke_blp.response(200, PokemonSchema)
def get_pokemon_by_name(name):
    return get_or_fetch_pokemon_by_name(name)
