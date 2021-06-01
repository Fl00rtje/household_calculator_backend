from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from conf import db_credentials

connection_string = f"postgresql://{db_credentials['user']}:{db_credentials['password']}@localhost:5432/household_calculator"
engine = create_engine(connection_string, echo=False)
Session = sessionmaker(bind=engine)

Base = declarative_base()