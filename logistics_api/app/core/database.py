from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from .config import settings

DATABASE_URL = settings.DATABASE_URL

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#autocommit=False, only developer will commit, no automatic commit
#autoflush=False, flush is manual
#bind=engine, bind the engine to the session

Base = declarative_base()

#DI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

