import os

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


POSTGRES_USER = os.environ.get("APP_POSTGRES_USER")
POSTGRES_PASSWORD = os.environ.get("APP_POSTGRES_PASSWORD")
POSTGRES_SERVER = os.environ.get("APP_POSTGRES_SERVER")
POSTGRES_PORT = os.environ.get("POSTGRES_PORT", 5432)
POSTGRES_DB = os.environ.get("APP_POSTGRES_DB")

db_uri = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"


engine = create_engine(db_uri, pool_pre_ping=True)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine, expire_on_commit=False)
