from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import settings
from tables import Base





engine = create_engine(
    settings.settings.database_url,
    connect_args={'check_same_thread': False},
)

Session = sessionmaker(
    engine,
    autoflush=False,
)


def get_session():
    session = Session()
    try:
        yield session
    finally:
        session.close()
