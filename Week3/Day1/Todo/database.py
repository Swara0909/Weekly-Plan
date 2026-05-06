#Used to connect your Python app to the database
from sqlalchemy import create_engine

#Used to create database sessions (like transactions) like Insert, update, delete
from sqlalchemy.orm import sessionmaker

#Used to create models (tables) in Python
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "postgresql+psycopg2://neondb_owner:npg_H5ZL7yicVfja@ep-silent-wave-amaptmlk-pooler.c-5.us-east-1.aws.neon.tech/neondb?sslmode=require"

#This actually connects to the database
engine = create_engine(DATABASE_URL)

# autocommit=False → you manually commit changes
# autoflush=False → changes won’t auto-save
# bind=engine → connect session to DB
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # used to create session factory

# This is used to create database tables (models)
Base = declarative_base()

