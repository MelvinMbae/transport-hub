from main import sort_by_daily_rental_fee_asc
from main import sort_by_daily_rental_fee_desc
from main import find_all_available_cars
from main import sort_by_driver_ratings
from main import sort_by_experience


import click

@click.command()

@click.option("--option", prompt="""
1. Filter available cars by daily fee(Lowest => Highest)
2. Filter available cars by daily fee(Highest => Lowest)
3. Filter by availability
4. Filter by average driver rating(Highest to Lowest)
5. Filter by years of experience(Highest to Lowest)

Select preferred option (1, 2):
""")

def filter_by_rental_fee(option):
    match option:
        case "1":    
            sort_by_daily_rental_fee_asc()
        case "2":
            sort_by_daily_rental_fee_desc()
        case "3":
            find_all_available_cars()
        case "4":
            sort_by_driver_ratings()    
        case "5":
            sort_by_experience()
            
filter_by_rental_fee()