import click

from main import potential_monthly_revenue
from main import monthly_revenue_on_available_cars
from main import monthly_revenue_lost_on_unavailable_cars

@click.command()

@click.option('--request', prompt="""
1. Show me the potential revenue report on all cars in the system
2. Show me the revenue report on available cars
3. Show me the revenue lost on all unavailable cars

Select Request (1,2...)
""")

def fetch_monthly_revenue(request):
    match request:
        case "1":
            potential_monthly_revenue()
        case "2":
            monthly_revenue_on_available_cars()
        case "3":
            monthly_revenue_lost_on_unavailable_cars()
            
fetch_monthly_revenue()