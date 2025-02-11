import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from config_data.config import (DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT,
                                DB_TESTS, DB_USER)


@pytest.fixture
def get_session():
    db_name = "bakery_vk_api_bot_tests"
    engine = create_engine(
        f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{db_name}"
    )
    Base = declarative_base()
    Session = sessionmaker(bind=engine)
    session = Session()
    return session