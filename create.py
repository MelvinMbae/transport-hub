import click

from create_driver import createDriver
from create_car import createCar

@click.command()

@click.option("--task", prompt="""
1. Create a Driver
2. Create a Car

Select Task:
""")

def main(task):
    match task:
        case "1":
            createDriver()
        case "2":
            createCar()
    
main()