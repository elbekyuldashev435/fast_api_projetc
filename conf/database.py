from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine


DATABASE_URL = "postgresql://postgres:Qwerty2109@localhost/fast_api_project"

engine = create_engine(DATABASE_URL)

Base = declarative_base()
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)