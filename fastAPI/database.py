from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# The connection string for your MySQL database
# Format: "mysql+mysqlconnector://user:password@host:port/database_name"
DATABASE_URL = "mysql+mysqlconnector://root:joychema%40254@localhost:3307/deliverdb"

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a session to interact with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for our SQLAlchemy models
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()