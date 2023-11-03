import click

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Car

engine = create_engine('sqlite:///transport_hub.db')

Session = sessionmaker(bind=engine)
session=Session()

def createCar():
    try:
        @click.command()

        @click.option("--model", prompt="Enter model name")
        @click.option("--make", prompt="Enter make")
        @click.option("--year", prompt="Enter year")
        @click.option("--color", prompt="Enter color")
        @click.option("--licence_plate", prompt="Enter plate number")
        @click.option("--car_mileage", prompt="Enter mileage in Kms")
        @click.option("--fuel_type", prompt="Enter fuel_type")
        @click.option("--seat_capacity", prompt=("Enter number of seats"))
        @click.option("--daily_rental_fee", prompt=("Enter daily fee"))
        @click.option("--monthly_rental_fee", prompt=("Enter monthly fee"))
        @click.option("--availability", prompt=("Available immediately"))
        @click.option("--driver_id", prompt=("Enter driver ID"))


        def create_car(model, make, year, color, licence_plate, car_mileage, fuel_type, seat_capacity, daily_rental_fee, monthly_rental_fee, availability, driver_id):
            car1 = Car(
                model=model,
                make=make,
                year=year,
                color=color,
                licence_plate=licence_plate,
                car_mileage=int(car_mileage),
                fuel_type=fuel_type,
                seat_capacity=int(seat_capacity),
                daily_rental_fee=float(daily_rental_fee),
                monthly_rental_fee=float(monthly_rental_fee),
                availability=bool(availability),
                driver_id=int(driver_id)
            )
            
            session.add(car1)
            session.commit()
            
            print(f"{model}, {make} created")
            
        create_car()
        
    except Exception as e:
        print("Could not create car: \n", e)

