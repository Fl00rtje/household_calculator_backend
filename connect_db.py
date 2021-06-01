from conf import db_credentials
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData

connection_string = f"postgresql://{db_credentials['user']}:{db_credentials['password']}@localhost:5432/household_calculator"
engine = create_engine(connection_string, echo=False)
engine.connect()


meta = MetaData()

users = Table(
   'users', meta,
   Column('id', Integer, primary_key = True),
   Column('first_name', String),
   Column('last_name', String),
   # Column('email_address', String),
)

meta.drop_all(engine)
meta.create_all(engine)
