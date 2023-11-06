import click
from main import remove_driver, remove_car, remove_review

@click.command()

@click.option("--selection", prompt="""
Are you sure you want to proceed(Y/N)?
""")

def warning_prompt(selection):
    if selection.lower() == "y":
        delete_from_db()        
    elif selection.lower() == "n":
        click.echo(click.style("Process exited", fg='green'))    
    else:
        click.echo(click.style("Invalid Option Selected", fg='red'))
        
def delete_from_db():
    task = click.prompt(click.style("""
WARNING!! THIS PROCESS IS IRREVERSIBLE
1. Delete a car by id
2. Delete a driver by id
3. Delete a review by id

Select Task: (eg. Select as 1, 2...)
""", fg= "red"))
    
    match task:
        case "1":
            car_id=int(input("What car do you want to delete eg.1,2,3 ? "))
            remove_car(car_id)
            click.echo(click.style("Car Deleted Successfully", fg="green"))
            
        case "2":
            driver_id=int(input("What driver do you want to delete eg.1,2,3 ? "))
            remove_driver(driver_id)
            click.echo(click.style("Driver Deleted Successfully", fg="green"))
                        
        case "3":
            review_id=int(input("What review do you want to delete eg.1,2,3 ? "))
            remove_review(review_id)
            click.echo(click.style("Review Deleted Successfully", fg="green"))
            
        case _:
            click.echo(click.style("Invalid Task Selected"))
            
warning_prompt()

       