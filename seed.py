from faker import Faker

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

import random

from models import Driver_Review
from models import Driver
from models import Car

engine = create_engine('sqlite:///transport_hub.db')

Session = sessionmaker(bind=engine)
session=Session()

#clear our db first before running python seed.py
session.query(Driver).delete()
session.commit()

fake = Faker()

drivers = [
    Driver(
        name=fake.name(),
        email=fake.email(),
        gender=random.choice(['Male', 'Female']),
        date_of_birth=fake.date_of_birth(minimum_age=23, maximum_age=60),
        age=fake.random_int(min=23, max=60),
        years_of_experience=fake.random_int(min=1, max=20)
    )
for _ in range(50)]    

session.bulk_save_objects(drivers)
session.commit()
session.close()