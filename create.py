import click

from create_driver import createDriver
from create_car import createCar
from create_review import createReview

@click.command()

@click.option("--task", prompt="""
1. Create a Driver
2. Create a Car
3. Create a Review

Select Task (eg. Select as 1, 2...):
""")

def main(task):
    match task:
        case "1":
            createDriver()
        case "2":
            createCar()
        case "3":
            createReview()
    
main()