import click
from datetime import date

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Driver

engine = create_engine('sqlite:///transport_hub.db')

Session = sessionmaker(bind=engine)
session=Session()

def createDriver():
    try:
        @click.command()

        @click.option("--name", prompt="Enter driver name")
        @click.option("--email", prompt="Enter email address")
        @click.option("--gender", prompt="Enter gender")
        @click.option("--date_of_birth", prompt=("Enter date of birth"))
        @click.option("--age", prompt=("Enter age"))
        @click.option("--years_of_experience", prompt="Enter years of experience")

        def create_driver(name, email, gender, date_of_birth, age, years_of_experience):
            driver1 = Driver(
                name=name,
                email=email,
                gender=gender,
                date_of_birth=date.fromisoformat(date_of_birth),
                age=int(age),
                years_of_experience=int(years_of_experience)
            )
            
            session.add(driver1)
            session.commit()
            
            print(f"Driver {name} with {years_of_experience} years experience added to database")
            
        create_driver()

    except Exception as e:
        print("Error\n", e)
        

