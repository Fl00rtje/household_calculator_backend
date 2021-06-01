from v5 import User, House, Car, Data
from base import Session, engine, Base


# 2 - generate database schema
Base.metadata.create_all(engine)

# 3 - create a new session
session = Session()

# 4 - create users
floor = User("Floor", "Harmsen", "floor@harmsen.nl")
tom = User("Tom", "Harmsen", "tom@kat.nl")
sam = User("Sam", "Harmsen", "sam@kat.nl")

# 5 - create houses
house_1 = House(1000, 100)
house_2 = House(1200, 90)

# 6 - create cars
car_1 = Car(40, 38, 30, 10)
car_2 = Car(50, 48, 0, 0)
car_3 = Car(60, 28, 0, 0)

# 7 - create data objects
data_1 = Data(floor)
data_2 = Data(sam)
data_3 = Data(tom)

data_1.house = house_1
data_1.car = car_1

data_2.house = house_1
data_2.car = car_2

data_3.house = house_1
data_3.car = car_3


# 9 - persists data
session.add(floor)
session.add(tom)
session.add(sam)
session.add(house_1)
session.add(house_2)
session.add(car_1)
session.add(car_2)
session.add(data_1)
session.add(data_2)
session.add(data_3)

# 10 - commit and close session
session.commit()
session.close()