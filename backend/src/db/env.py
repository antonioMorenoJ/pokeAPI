from alembic import context
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from aps.db import get_db_string
from aps.models.rest_item import BaseSQL
from aps.settings import settings

from src.models.infoPokemon import InfoPokemon # noqa F401
from src.models.pokemon import Pokemon # noqa F401
from src.models.user import User# noqa F401


#
# TODO: Add here your database models
#
# from src.models.user import User # noqa F401

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = BaseSQL.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.
if not settings.ENABLE_MULTICLIENT:
    config.set_main_option('sqlalchemy.url', get_db_string())


def include_object(_object, name: str, type_: str, _reflected, _compare_to) -> bool:  # noqa: ANN001
    """
    Hook that checks whether a table object should be included or not.
    Basically this function skips the MultiClient tables in the autogenerate process

    :param _object: no usage
    :param name: Name of the object (eg. 'permissions')
    :param type_: Type of the object (eg. 'table', 'column'...)
    :param _reflected: no usage
    :param _compare_to: no usage
    """
    if type_ == 'table':
        return name not in ['user_sa', 'customer', 'customer_domain']
    else:
        return True


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option('sqlalchemy.url')
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={'paramstyle': 'named'},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix='sqlalchemy.',
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            include_object=include_object,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
