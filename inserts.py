from v5 import User
from base import Session, engine, Base


# 2 - generate database schema
Base.metadata.create_all(engine)

# 3 - create a new session
session = Session()

# 4 - create users
floor = User("Floor", "Harmsen", "floor@harmsen.nl")
tom = User("Tom", "Harmsen", "tom@kat.nl")
sam = User("Sam", "Harmsen", "sam@kat.nl")

# 9 - persists data
session.add(floor)
session.add(tom)
session.add(sam)

# 10 - commit and close session
session.commit()
session.close()