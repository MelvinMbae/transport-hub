import click

from main import get_rating_by_driver_id

from models import Driver_Review

@click.command()
        
def driver_rating():
    task = click.prompt("""
Y. Search for a driver review by their id
N. Exit

Select Y/N
""")
    if task.lower() == "y":
        driver_id = int(input("What is the driver id: "))
        get_rating_by_driver_id(driver_id)
    elif task.lower() == "n":
        click.echo(click.style("Process exited", fg='green'))
    else:
        click.echo(click.style("Invalid Option Selected", fg='red'))

driver_rating()