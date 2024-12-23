from sqlmodel import Field, Session, create_engine
from config import settings


engine = create_engine(settings.dev_db_url)

def get_session():
    with Session(bind = engine,autocommit=False,autoflush=False) as db:
        yield db


    

