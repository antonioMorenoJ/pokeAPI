from contextlib import contextmanager

from aps.db import get_db_string
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine, NullPool

engine = create_engine(get_db_string(), echo=False, poolclass=NullPool)

@contextmanager
def get_db_session():
    """
    Create a new session for the database.
    """
    Session = sessionmaker(engine, expire_on_commit=False)
    session = Session()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()