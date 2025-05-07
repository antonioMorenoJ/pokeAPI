import requests
from flask_smorest import abort
from backend.src.utils.db import get_db_session
from ..models.pokemon import Pokemon
from ..utils.db import get_db_session
from ..models.infoPokemon import InfoPokemon
BASE_URL = "https://pokeapi.co/api/v2"
def fetch_pokemon(name):
    with get_db_session() as session:
        pokemon = session.query(Pokemon).filter_by(poke_name = name).first()

        if not pokemon:
            url = f"{BASE_URL}/pokemon/{name}"

            response = requests.get(url)
            if response.status_code != 200:
                abort(404, message="Pokemon, {name} not found")

            data = response.json()

            poke_name = data.get("name")

            pokemon = Pokemon(poke_name = poke_name)
            session.add(pokemon)
            session.commit()
        else:
            pokemon_name = pokemon.poke_name

    url = f"{BASE_URL}/pokemon/{pokemon_name}"
    response = requests.get(url)
    if response.status_code != 200:
        abort(404, message="Pokemon, {poke_name} not found")
    data = response.json()

    poke_info = InfoPokemon(
        poke_name = data.name,
        move = data["moves"][0],
    )
    session.add(poke_info)
    session.commit()

    return{
        "pokemon": pokemon.name,
        "move": poke_info.move,
    }