from dynaconf import Dynaconf
import os
from aps.settings import settings

# Imprimir el entorno actual
print("Entorno actual:", os.getenv('FLASK_ENV'))  # Verifica que se esté estableciendo el entorno correctamente

# Imprimir DB_HOST cargado
print("DB_HOST:", settings.DB_HOST)  # Verifica que el valor esté siendo cargado

# Carga el archivo settings.toml y .env
settings = Dynaconf(
    settings_files=["backend/configs/settings.toml"],
    load_dotenv=True,  # Asegúrate de que cargue .env
)

# Verifica qué entorno se está usando
print("Entorno cargado:", settings.current_env)

# Verifica el valor de DB_HOST
print("DB_HOST:", settings.get("DB_HOST"))
