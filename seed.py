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

driver_list = []
for _ in range(50):
    drivers = Driver(
        name=fake.name(),
        email=fake.email(),
        gender=random.choice(['Male', 'Female']),
        date_of_birth=fake.date_of_birth(minimum_age=23, maximum_age=60),
        age=fake.random_int(min=23, max=60),
        years_of_experience=fake.random_int(min=1, max=20)
    )

    session.add(drivers)
    session.commit()
    driver_list.append(drivers)

#populate our cars table

#first clear the table everytime we run ssd.py
session.query(Car).delete()
session.commit()

car_makes = ['Toyota', 'Honda', 'Ford', 'Chevrolet', 'BMW', 'Mercedes-Benz', 'Audi', 'Volkswagen']
car_models = ['Camry', 'Civic', 'F-150', 'Silverado', '3 Series', 'E-Class', 'A4', 'Golf']

for driver in driver_list:
    cars =Car(
        make=random.choice(car_makes),
        model=random.choice(car_models),
        year=fake.random_int(min=2014, max=2023),
        color=fake.color_name(),
        licence_plate=fake.license_plate(),
        car_mileage=fake.random_int(min=1000, max=150000),
        fuel_type=random.choice(['Petrol', 'Diesel', 'Electric', 'Hybrid', 'Gas']),
        seat_capacity=fake.random_int(min=4, max=7),
        daily_rental_fee=fake.random_int(min=5000, max=10000),
        monthly_rental_fee=fake.random_int(min=80000, max=250000),
        availability=fake.boolean(chance_of_getting_true=80),
        driver_id=driver.id
    )


    session.add(cars)
    session.commit()
    
session.query(Driver_Review).delete()
session.commit()


for driver in driver_list:
    # Generate a random number of reviews per driver
    num_reviews = random.randint(0, 3)
    
    list_of_reviews = [
    f"{driver.name} was very punctual and polite. The car was clean and comfortable. I had a great experience.",
    f"Outstanding service! {driver.name} was professional and the car was in excellent condition. Will definitely use this service again.",
    f"{driver.name} arrived a bit late, but the ride was smooth, and the car was decent. An average experience.",
    "The driver was okay, but the car had a weird noise. It made me a bit uncomfortable during the ride."
    f"I had a pleasant trip with {driver.name}. The car was well-maintained, and the driver was friendly and helpful.",
    f"Overall, a good experience. {driver.name} was courteous, and the car was in good shape. I'd use this service again.",
    f"Exemplary service! {driver.name} was on time, and the car was pristine. Highly recommended.",
    f"Absolutely fantastic! {driver.name} was very friendly, and the car was spotless. I couldn't have asked for a better experience.",
    f"{driver.name} was extremely professional."
]
    for _ in range(num_reviews):
        reviews = Driver_Review(
            rating=random.randint(3, 5),
            comment=random.choice(list_of_reviews),
            driver_id=driver.id
        )

        session.add(reviews)
        session.commit()



session.close()

