import click
from main import get_all_drivers
from main import get_all_cars
from main import find_all_available_cars
from main import find_car_by_driver_id


@click.command()

@click.option("--option", prompt="""
1. Give me a List of all Drivers
2. Give me a List of all Cars
3. Give me a List of all Available Cars
4. Find car by driver id

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
        case "4":
            driver_id = int(input("What is the driver ID? "))
            click.echo(click.style(find_car_by_driver_id(driver_id),fg='green'))
            
request_list()