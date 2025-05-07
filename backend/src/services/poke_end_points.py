from flask_smorest import Blueprint

from backend.src.models.infoPokemon import infoPokemonSchema
from backend.src.models.pokemon import Pokemon, PokemonSchema

poke_blp = ("Pokemon", __name__, description = "Pokemon description")

@blp.route("/pokemon", methods=["GET"])
@blp.arguments(PokemonSchema, location = "query")
@blp.response(200, infoPokemonSchema)

def get_pokemon(args):
    pokemon_name = args["pokemon_name"]
