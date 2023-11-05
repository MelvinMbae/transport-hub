import click
from main import remove_driver, remove_car

@click.command()

@click.option("--input", prompt="""
Y. Yes
N. No

Are you sure you want to proceed(Y/N)?
""")

def warning_prompt(input):
    if input == "Y":     
        delete_from_db()
        
    elif input == "N":
        click.echo("Process exited")
        
    else:
        click.echo("Invalid Option Selected")
        
def delete_from_db():
    task = click.prompt("""
1. Delete a car by id
2. Delete a Driver by id

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

       