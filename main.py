from models import Driver, Driver_Review, Car

from sqlalchemy.orm import sessionmaker

from sqlalchemy import create_engine, func, desc, text

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
    car = session.query(Car.make, Car.model, Car.color, Car.licence_plate).filter(Car.driver_id == n).first()
    print(f"""
Car make: {car.make}
model{car.model}
color:{car.color}
plate no:{car.licence_plate}""")

# monthly revenue of the cars in our db
def potential_monthly_revenue():
    revenue_on_all_cars = session.query(func.sum(Car.monthly_rental_fee)).scalar()
    print(f"Potential revenue on all cars is Kshs.{revenue_on_all_cars}")
    
def monthly_revenue_on_available_cars():
    revenue_on_available_cars = session.query(func.sum(Car.monthly_rental_fee)
        ).filter(Car.availability==1).scalar()
    print(f"Potential revenue on available cars is Kshs.{revenue_on_available_cars}")
     
def monthly_revenue_lost_on_unavailable_cars():
    revenue_on_unavailable_cars = session.query(func.sum(Car.monthly_rental_fee)).filter(Car.availability==0).scalar()
    print(f"Potential revenue on unavailable cars is Kshs.{revenue_on_unavailable_cars}")

# Filter by fee
def sort_by_daily_rental_fee_asc():
    cars = session.query(Car.id, Car.model, Car.make, Car.daily_rental_fee, Car.availability
        ).order_by(Car.daily_rental_fee).filter(Car.availability ==1).all()
    
    for car in cars:
        print(f"{car.model}{car.make}, Car ID {car.id} daily rental fee is Kshs.{car.daily_rental_fee}")

def sort_by_daily_rental_fee_desc():
    cars = session.query(Car.id, Car.model, Car.make, Car.daily_rental_fee,Car.availability
        ).order_by(desc(Car.daily_rental_fee)).filter(Car.availability ==1).all()
    
    for car in cars:
        print(f"{car.model} {car.make}, Car ID {car.id} daily rental fee is Kshs.{car.daily_rental_fee}")
        
def get_cars_by_fuel_type(fuel_type):
    cars = session.query(Car.id, Car.make).filter(Car.fuel_type == fuel_type).all()
    for car in cars:
        print(f"Car{car.id}: {car.make}")

# Delete a car from the Data base
def remove_car(car_id):
    car = session.query(Car).filter(Car.id == car_id).first()
    
    if car:
        session.delete(car)
        session.commit()
    else:
        print("No such car exists.")
    
#DRIVER METHODS
#getting all our drivers
def get_all_drivers():
    drivers = session.query(Driver).all()
    
    for driver in drivers:
        print(driver)

# sorting our drivers by their years of experience
def sort_by_experience():
    years_of_exp_asc = session.query(Driver).order_by(desc(Driver.years_of_experience)).all()
    
    for years in years_of_exp_asc:
        print(f"Driver {years.id}: {years.name} has an experience of {years.years_of_experience} years")

# Delete driver by ID
def remove_driver(driver_id):
    driver = session.query(Driver).filter(Driver.id == driver_id).first()
    
    if driver:
        session.delete(driver)
        session.commit()
    else:
        print("No such driver exists.")
    
# REVIEW METHODS
# get a driver rating by the driver_id
def get_rating_by_driver_id(driver_id):
    ratings = session.query(Driver_Review.rating, Driver_Review.comment
            ).filter(Driver_Review.driver_id == driver_id).all()
    
    for rating in ratings:
        print(rating)

# sort our drivers by their average rating        
def sort_by_driver_ratings():
    drivers = session.query(
        Driver_Review.driver_id,
        func.avg(Driver_Review.rating).label("average_rating")
        ).group_by(Driver_Review.driver_id).order_by(desc(text("average_rating"))).all()
    
    for driver in drivers:
        driver_id, average_rating = driver
        print(f"Driver ID: {driver_id}, Average Rating: {round(average_rating,2)}")
        
# Delete a review
        
        

        
    