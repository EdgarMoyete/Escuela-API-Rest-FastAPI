from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import DATABASE_CONNECTION_URI

engine = create_engine(DATABASE_CONNECTION_URI)
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
base = declarative_base()

def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()

# crear las tablas de la base de datos
# models.Base.metadata.create_all(bind=engine)