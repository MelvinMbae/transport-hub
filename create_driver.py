import click

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Driver

engine = create_engine('sqlite:///transport_hub.db')

Session = sessionmaker(bind=engine)
session=Session()

@click.command()

@click.option("--name", prompts="Enter driver name: ")
@click.option("--email", prompts="Enter email address: ")
@click.option("--gender", prompts="Enter gender: ")
@click.option("--date_of_birth", prompts="Enter date of birth: ")
@click.option("--age", prompts="Enter age: ")
@click.option("--years_of_experience", prompts="Enter years of experience: ")

def create_car(name, email, gender, date_of_birth, age, years_of_experience):
    driver1 = Driver(
        name=name,
        email=email,
        gender=gender,
        date_of_birth=date_of_birth,
        age=age,
        years_of_experience=years_of_experience
    )
    
    session.add(driver1)
    session.commit()
    
    print(f"Driver {name} with {years_of_experience}years experience added to database")
    
create_car()
