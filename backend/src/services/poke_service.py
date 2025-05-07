from backend.src.utils.db import get_db_session
from ..utils.db import get_db_session
BASE_URL = "https://pokeapi.co/api/v2"
def get_pokemon(name):
    with get_db_session() as session:
        pokemon = session.query(Pokemon).filter_by(poke_name = name).first()

