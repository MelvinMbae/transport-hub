import click
from main import remove_driver, remove_car

@click.command()

@click.option("--selection", prompt="""
Are you sure you want to proceed(Y/N)?
""")

def warning_prompt(selection):
    if selection == "Y" or "y":
        delete_from_db()        
    elif selection == "N" or "n":
        click.echo("Process exited")        
    else:
        click.echo("Invalid Option Selected")
        
def delete_from_db():
    task = click.prompt("""
WARNING!! THIS PROCESS IS IRREVERSIBLE
1. Delete a car by id
2. Delete a driver by id

Select Task: (eg. Select as 1, 2...)
""")
    
    match task:
        case "1":
            car_id=int(input("What car do you want to delete eg.1,2,3 ? "))
            remove_car(car_id)
            
        case "2":
            driver_id=int(input("What driver do you want to delete eg.1,2,3 ? "))
            remove_driver(driver_id)
            
warning_prompt()

       