import requests
from backend.src.db.env import session
from backend.src.models.pokemon.pokemon import Pokemon

def get_or_fetch_pokemon_by_name(name: str) -> Pokemon:
    pokemon = session.query(Pokemon).filter_by(name=name.lower()).first()
    if pokemon:
        return pokemon

    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError(f"Pokémon '{name}' no encontrado en la PokéAPI")

    data = response.json()
    types = [t["type"]["name"] for t in data["types"]]
    type_str = "/".join(types)
    generation = "unknown"

    pokemon = Pokemon(
        name=data["name"],
        type=type_str,
        generation=generation
    )
    session.add(pokemon)
    session.commit()
    return pokemon
