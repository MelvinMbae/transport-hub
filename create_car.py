import click

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Car

engine = create_engine('sqlite:///transport_hub.db')

Session = sessionmaker(bind=engine)
session=Session()

@click.command()

@click.option("--model", prompts="Enter model name: ")
@click.option("--make", prompts="Enter make: ")
@click.option("--year", prompts="Enter year: ")
@click.option("--color", prompts="Enter color: ")
@click.option("--licence_plate", prompts="Enter plate number: ")
@click.option("--car_mileage", prompts="Enter mileage in Kms: ")
@click.option("--fuel_type", prompts="Enter fuel_type: ")
@click.option("--seat_capacity", prompts=int("Enter number of seats: "))
@click.option("--daily_rental_fee", int(prompts="Enter daily fee: "))
@click.option("--monthly_rental_fee", int(prompts="Enter monthly fee: "))
@click.option("--availability", bool(prompts="Available immediately: "))
@click.option("--driver_id", int(prompts="Enter driver ID: "))


def create_car(model, make, year, color, licence_plate, car_mileage, fuel_type, seat_capacity, daily_rental_fee, monthly_rental_fee, availability, driver_id):
    car1 = Car(
        model=model,
        make=make,
        year=year,
        color=color,
        licence_plate=licence_plate,
        car_mileage=car_mileage,
        daily_rental_fee=daily_rental_fee,
        monthly_rental_fee=monthly_rental_fee,
        availability=availability,
        driver_id=driver_id
    )
    
    session.add(car1)
    session.commit()
    
    print(f"{model}, {make} created")
    
create_car()
