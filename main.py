from models import Driver, Driver_Review, Car

from sqlalchemy.orm import sessionmaker

from sqlalchemy import create_engine, func, desc

engine = create_engine('sqlite:///transport_hub.db')

# Initialize a session
Session = sessionmaker(bind=engine)
session=Session()

#CAR METHODS

# method to print all cars in our db
def get_all_cars():
    cars = session.query(Car).all()
    for car in cars:
        print(car)

# method to return all available cars
def find_all_available_cars():
    cars = session.query(Car)
    available_cars = cars.filter(Car.availability == 1).all()
    for available_car in available_cars:
        print(available_car)

#count all available/unavailable cars
def find_number_of_available_cars(x):
    
    if x == 0:
        unavailable_cars_count = session.query(func.count(Car.id)).filter(Car.availability == 0).scalar()
        return f"{unavailable_cars_count} cars currently unavailable"
    
    else:
        available_cars_count = session.query(func.count(Car.id)).filter(Car.availability == 1).scalar()
        return f"{available_cars_count} cars currently available"

# find car a particular by the driver id
def find_car_by_driver_id(n):
    car = session.query(Car.make).filter(Car.driver_id == n).first()
    return car

# monthly revenue of the cars in our db
def potential_monthly_revenue():
    revenue_on_all_cars = session.query(func.sum(Car.monthly_rental_fee)).scalar()
    print(f"Potential revenue on all cars is Kshs.{revenue_on_all_cars}")
    
def monthly_revenue_on_available_cars():
    revenue_on_available_cars = session.query(func.sum(Car.monthly_rental_fee)).filter(Car.availability==1).scalar()
    print(f"Potential revenue on available cars is Kshs.{revenue_on_available_cars}")
     
def monthly_revenue_lost_on_unavailable_cars():
    revenue_on_unavailable_cars = session.query(func.sum(Car.monthly_rental_fee)).filter(Car.availability==0).scalar()
    print(f"Potential revenue on unavailable cars is Kshs.{revenue_on_unavailable_cars}")

# Filter by fee
def sort_by_daily_rental_fee_asc():
    daily_fee_ascending = session.query(Car).order_by(Car.daily_rental_fee).all()
    for daily_fee in daily_fee_ascending:
        print(f"{Car.id} daily rental fee is Kshs.{daily_fee}")

def sort_by_daily_rental_fee_desc():
    daily_fee_descending = session.query(Car).order_by(Car.daily_rental_fee).desc().all()
    for daily_fee in daily_fee_descending:
        print(f"{Car.id} daily rental fee is Kshs.{daily_fee}")

# Delete a car from the Data base
def remove_car(car_id):
    car = session.query(Car).filter(Car.id == car_id).first()
    if car:
        session.delete(car)
        session.commit()
    else:
        print("No such car exists.")
    
#Driver Methods
#getting all our drivers
def get_all_drivers():
    drivers = session.query(Driver).all()
    for driver in drivers:
        print(driver)

# sorting our drivers by their years of experience
def sort_by_experience():
    years_of_exp_asc = session.query(Driver).order_by(Driver.years_of_experience).all()
    for years in years_of_exp_asc:
        print(f"Driver {Driver.id}: {Driver.name} has an experience of {years}")

# Delete driver by ID
def remove_driver(driver_id):
    driver = session.query(Driver).filter(Driver.id == driver_id).first()
    if driver:
        session.delete(driver)
        session.commit()
    else:
        print("No such driver exists.")
    
# remove_driver(50)

