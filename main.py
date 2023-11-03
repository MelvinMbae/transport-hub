from models import Driver, Driver_Review, Car

from sqlalchemy.orm import sessionmaker

from sqlalchemy import create_engine, func

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

get_all_cars()

# method to return all available cars
def find_all_available_cars():
    cars = session.query(Car)
    available_cars = cars.filter(Car.availability == 1).all()
    return available_cars

print(find_all_available_cars())

#count all available/unavailable cars
def find_number_of_available_cars(x):
    
    if x == 0:
        unavailable_cars_count = session.query(func.count(Car.id)).filter(Car.availability == 0).scalar()
        return f"{unavailable_cars_count} cars currently unavailable"
    
    else:
        available_cars_count = session.query(func.count(Car.id)).filter(Car.availability == 1).scalar()
        return f"{available_cars_count} cars currently available"

print(find_number_of_available_cars(1))

# find car a particular by the driver id
def find_car_by_driver_id(n):
    car = session.query(Car.make).filter(Car.driver_id == n).first()
    return car

print(find_car_by_driver_id(2))

# monthly revenue of the cars in our db
def monthly_revenue():
    revenue_on_all_cars = session.query(func.sum(Car.monthly_rental_fee)).scalar()
    revenue_on_available_cars = session.query(func.sum(Car.monthly_rental_fee)).filter(Car.availability==1).scalar()
    revenue_on_unavailable_cars = session.query(func.sum(Car.monthly_rental_fee)).filter(Car.availability==0).scalar()
    return f"Potential revenue on all cars is Kshs.{revenue_on_all_cars} but we are only raking in Kshs.{revenue_on_available_cars}. We are missing Kshs.{revenue_on_unavailable_cars}"

print(monthly_revenue())

def sort_by_daily_rental_fee():
    return session.query(Car).order_by(Car.daily_rental_fee).all()

print(sort_by_daily_rental_fee())

# Delete a car from the Data base
def remove_car(car_id):
    car = session.query(Car).filter(Car.id == car_id).first()
    if car:
        session.delete(car)
        session.commit()
    else:
        print("No such car exists.")
    
remove_car(50)


#Driver Methods
#getting all our drivers
def get_all_drivers():
    drivers = session.query(Driver).all()
    for driver in drivers:
        print(driver)

get_all_drivers()

# sorting our drivers by their years of experience
def sort_by_experience():
    return session.query(Driver).order_by(Driver.years_of_experience).all()

print(sort_by_experience())

def remove_driver(driver_id):
    driver = session.query(Driver).filter(Driver.id == driver_id).first()
    if driver:
        session.delete(driver)
        session.commit()
    else:
        print("No such driver exists.")
    
remove_driver(50)

