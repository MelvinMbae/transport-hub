import click

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Driver_Review

engine = create_engine('sqlite:///transport_hub.db')

Session = sessionmaker(bind=engine)
session=Session()

def createReview():
    try:
        @click.command()

        @click.option("--rating", prompt="Enter your Driver rating")
        @click.option("--comment", prompt="Enter Comment")
        @click.option("--driver_id", prompt=("Enter driver ID"))

        def create_review(rating, comment, driver_id):
            review = Driver_Review(
                rating=int(rating),
                comment=comment,
                driver_id=driver_id
                
            )
            session.add(review)
            session.commit()
            
            click.echo(click.style("Review successfully added", fg='green'))
            
        create_review()

    except Exception as e:
        print("Error:\n", e)