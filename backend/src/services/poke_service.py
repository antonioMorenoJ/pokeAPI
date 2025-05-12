import requests
from flask_smorest import abort
from ..models.pokemon.pokemon import Pokemon
from ..utils.db import get_db_session
from ..models.infoPokemon.infoPokemon import InfoPokemon
BASE_URL = "https://pokeapi.co/api/v2"

def fetch_all_pokemon():
    """
    Fetch all Pokemon from the database or a default list if the database is empty
    """
    with get_db_session() as session:
        # Get all Pokemon from the database
        pokemon_list = session.query(Pokemon).all()

        # If the database is empty, return a default list of popular Pokemon
        if not pokemon_list:
            default_pokemon = ["pikachu", "charizard", "bulbasaur", "squirtle", "jigglypuff"]
            pokemon_list = []

            for name in default_pokemon:
                # Fetch each Pokemon and add it to the list
                pokemon_data = fetch_pokemon(name)
                pokemon_list.append(pokemon_data)

            return pokemon_list

        # If we have Pokemon in the database, format them for the response
        result = []
        for pokemon in pokemon_list:
            # Get the associated info for this Pokemon
            info = session.query(InfoPokemon).filter_by(pokemon_name=pokemon.name).first()

            if info:
                result.append({
                    "pokemon": pokemon.name,
                    "type": pokemon.type,
                    "generation": pokemon.generation,
                    "move": info.move,
                    "image_url": pokemon.image_url
                })
            else:
                # If no info exists, just use the Pokemon data
                result.append({
                    "pokemon": pokemon.name,
                    "type": pokemon.type,
                    "generation": pokemon.generation,
                    "move": "unknown",
                    "image_url": pokemon.image_url
                })

        return result


# def fetch_pokemon(name):
#     with get_db_session() as session:
#         pokemon = session.query(Pokemon).filter_by(name = name).first()
#
#         if not pokemon:
#             url = f"{BASE_URL}/pokemon/{name}"
#
#             response = requests.get(url)
#             if response.status_code != 200:
#                 abort(404, message=f"Pokemon {name} not found")
#
#             data = response.json()
#
#             poke_name = data.get("name")
#
#             # Get the first type if available
#             poke_type = data["types"][0]["type"]["name"] if data.get("types") and len(data["types"]) > 0 else "unknown"
#
#             # Get generation info if available (defaulting to unknown)
#             generation = "unknown"
#
#             pokemon = Pokemon(
#                 name=poke_name,
#                 type=poke_type,
#                 generation=generation
#             )
#             session.add(pokemon)
#             session.commit()
#
#         # Get pokemon data from API
#         url = f"{BASE_URL}/pokemon/{name}"
#         response = requests.get(url)
#         if response.status_code != 200:
#             abort(404, message=f"Pokemon {name} not found")
#
#         data = response.json()
#
#         # Get the first move
#         move = data["moves"][0]["move"]["name"] if data.get("moves") and len(data["moves"]) > 0 else "unknown"
#
#         # Create or update info pokemon
#         poke_info = InfoPokemon(
#             pokemon_name = name,
#             move = move
#         )
#         session.add(poke_info)
#         session.commit()
#
#         return {
#             "pokemon": name,
#             "move": move
#         }


def get_first_generation(name):
    url = f"{BASE_URL}/pokemon-species/{name}"
    response = requests.get(url)
    if response.status_code != 200:
        abort(404, message=f"Pokemon {name} not found")

    species_data = response.json()
    generation = species_data.get("generation", {}).get("name", "unknown")
    return generation

def fetch_pokemon(name):
    with get_db_session() as session:
        pokemon = session.query(Pokemon).filter_by(name=name).first()

        if not pokemon:
            # Get basic Pokemon data
            pokemon_url = f"{BASE_URL}/pokemon/{name}"
            response = requests.get(pokemon_url)
            if response.status_code != 200:
                abort(404, message=f"Pokemon {name} not found")

            pokemon_data = response.json()

            # Get the latest generation for this Pokemon
            first_generation = get_first_generation(name)

            poke_name = pokemon_data.get("name")
            poke_type = pokemon_data["types"][0]["type"]["name"] if pokemon_data.get("types") else "unknown"
            move = pokemon_data["moves"][0]["move"]["name"] if pokemon_data.get("moves") else "unknown"

            # Get the image URL from sprites
            image_url = pokemon_data.get("sprites", {}).get("front_default")

            pokemon = Pokemon(
                name=poke_name,
                type=poke_type,
                generation=first_generation,
                image_url=image_url
            )
            session.add(pokemon)
            session.commit()


        # Create or update info pokemon
            poke_info = InfoPokemon(
                pokemon_name=name,
                move=move
            )
            session.add(poke_info)
            session.commit()
        else:
            # Get the latest data for this Pokemon to update the image URL
            pokemon_url = f"{BASE_URL}/pokemon/{name}"
            response = requests.get(pokemon_url)
            if response.status_code != 200:
                abort(404, message=f"Pokemon {name} not found")

            pokemon_data = response.json()

            # Update the image URL
            image_url = pokemon_data.get("sprites", {}).get("front_default")
            if image_url and pokemon.image_url != image_url:
                pokemon.image_url = image_url
                session.commit()

            poke_info = session.query(InfoPokemon).filter_by(pokemon_name=name).first()
            if not poke_info:
                # Get the move for this Pokemon
                move = pokemon_data["moves"][0]["move"]["name"] if pokemon_data.get("moves") else "unknown"

                poke_info = InfoPokemon(
                    pokemon_name=name,
                    move=move
                )
                session.add(poke_info)
                session.commit()

        return {
            "name": pokemon.name,
            "type": pokemon.type,
            "generation": pokemon.generation,
            "move": poke_info.move,
            "image_url": pokemon.image_url
        }
