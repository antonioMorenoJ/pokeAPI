import requests
from flask_smorest import abort
from ..models.pokemon.pokemon import Pokemon
from ..utils.db import get_db_session
from ..models.infoPokemon.infoPokemon import InfoPokemon
BASE_URL = "https://pokeapi.co/api/v2"
def fetch_pokemon(name):
    with get_db_session() as session:
        pokemon = session.query(Pokemon).filter_by(name = name).first()

        if not pokemon:
            url = f"{BASE_URL}/pokemon/{name}"

            response = requests.get(url)
            if response.status_code != 200:
                abort(404, message=f"Pokemon {name} not found")

            data = response.json()

            poke_name = data.get("name")

            # Get the first type if available
            poke_type = data["types"][0]["type"]["name"] if data.get("types") and len(data["types"]) > 0 else "unknown"

            # Get generation info if available (defaulting to unknown)
            generation = "unknown"

            pokemon = Pokemon(
                name=poke_name,
                type=poke_type,
                generation=generation
            )
            session.add(pokemon)
            session.commit()

        # Get pokemon data from API
        url = f"{BASE_URL}/pokemon/{name}"
        response = requests.get(url)
        if response.status_code != 200:
            abort(404, message=f"Pokemon {name} not found")

        data = response.json()

        # Get the first move
        move = data["moves"][0]["move"]["name"] if data.get("moves") and len(data["moves"]) > 0 else "unknown"

        # Create or update info pokemon
        poke_info = InfoPokemon(
            pokemon_name = name,
            move = move
        )
        session.add(poke_info)
        session.commit()

        return {
            "pokemon": name,
            "move": move
        }
