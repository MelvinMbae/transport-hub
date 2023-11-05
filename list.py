import click
from main import get_all_drivers, get_all_cars, find_all_available_cars
from main import get_all_cars
from main import find_all_available_cars


@click.command()

@click.option("--option", prompt="""
1. Give me a List of all Drivers
2. Give me a List of all Cars
3. Give me a List of all Available Cars

Select Option: (eg. Select as 1, 2...)
""")

def request_list(option):
    match option:
        case "1":
            get_all_drivers()
        case "2":
            get_all_cars()
        case "3":
            find_all_available_cars()
            
request_list()