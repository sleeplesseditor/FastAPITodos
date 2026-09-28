import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Option for Sqlite3 connection
# SQLALCHEMY_DATABASE_URL =  f"sqlite:///{os.path.join(BASE_DIR, 'todosapp.db')}"
# engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True, connect_args={'check_same_thread': False})

# Option for MySql connection
# MYSQL_DATABASE_URL = "mysql+pymysqyl"//root://exampleURL"
# engine = create_engine(MYSQL_DATABASE_URL, echo=True)

# Option for Postgres connection
POSTGRES_URL = "postgresql://postgres:exampleURL"
engine = create_engine(POSTGRES_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()