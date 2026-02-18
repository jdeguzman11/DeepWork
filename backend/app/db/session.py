
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# environment variable reading
DATABASE_URL = os.getenv("DATABASE_URL")

# engine creation: object that connects to database
engine = create_engine(DATABASE_URL)

# create SessionLocal - allows me to perform queries
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


class Base(DeclarativeBase):  # creation of Base class for models
    pass
