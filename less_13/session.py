from contextlib import contextmanager
from typing import ContextManager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from config import db_conf

engine = create_engine(db_conf.dsn)
DBSession = sessionmaker(bind=engine)


@contextmanager
def open_db_session(with_commit=False) -> ContextManager[Session]:
    session = DBSession()
    try:
        yield session
        if with_commit:
            session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
