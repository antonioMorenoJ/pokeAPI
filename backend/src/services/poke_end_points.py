from flask_smorest import Blueprint

from ..models.infoPokemon.infoPokemon import InfoPokemon
from ..models.infoPokemon.infoPokemonSchema import InfoPokemonSchema
from ..models.pokemon.pokemon import Pokemon
from ..models.pokemon.pokemon_schema import PokemonSchema
from ..services.poke_service import fetch_pokemon

poke_blp = Blueprint("Pokemon", __name__, url_prefix="/", description="Pokemon description")

@poke_blp.route("/pokemon/<string:pokemon_name>", methods=["GET"])
@poke_blp.response(200, InfoPokemonSchema)
def get_pokemon(pokemon_name):
    pokemon = fetch_pokemon(pokemon_name)
    return pokemon
