import click
from main import get_all_drivers, get_all_cars, find_all_available_cars

@click.command()

@click.option("--task", prompt="""
1. Give me a List of all Drivers
2. Give me a List of all Cars
3. Give me a List of all Available Drivers

Select Task: (eg. Select as 1, 2...)
""")

def request_list(task):
    match task:
        case "1":
            get_all_drivers()
        case "2":
            get_all_cars()
        case "3":
            print(find_all_available_cars())
            
request_list()