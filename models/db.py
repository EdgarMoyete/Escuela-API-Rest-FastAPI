from sqlalchemy import create_engine, MetaData

from config import DATABASE_CONNECTION_URI

engine = create_engine(DATABASE_CONNECTION_URI)
meta = MetaData()
conexion = engine.connect()