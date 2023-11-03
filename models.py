from sqlalchemy import create_engine
from sqlalchemy import (UniqueConstraint, Column, Integer, String, Float, Boolean, Date, ForeignKey)

from sqlalchemy.orm import relationship, backref


from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///transport_hub.db')

Base = declarative_base()

class Driver(Base):
    __tablename__ = 'drivers'
    __table_args__ = (
        UniqueConstraint('email', name='unique_email'),
    )

    id = Column(Integer, primary_key=True)
    name=Column(String)
    email = Column(String(50))
    gender=Column(String)
    date_of_birth=Column(Date)
    age=Column(Integer)
    years_of_experience=Column(Integer)
    reviews = relationship('Driver_Review', backref=backref('driver'))
    
    def __repr__(self):
        return f"Driver(id={self.id}, " + \
            f"name={self.name}, " + \
            f"years_of_experience = {self.years_of_experience})"
        
    
class Car(Base):
    __tablename__ = 'cars'
    __table_args__ = (UniqueConstraint('licence_plate',name='unique_licence_plate'),)
    
    id = Column(Integer, primary_key=True)
    make = Column(String)
    model = Column(String)
    year = Column(Integer)
    color = Column(String)
    licence_plate = Column(String)
    car_mileage= Column(Integer)
    fuel_type=Column(String)
    seat_capacity = Column(Integer)
    daily_rental_fee = Column(Float(precision=2))
    monthly_rental_fee = Column(Float(precision=2))
    availability = Column(Boolean)
    driver_id=Column(Integer, ForeignKey('drivers.id'))
    driver = relationship('Driver', backref=backref('car', uselist=False))
    
    def __repr__(self):
        return f"Car(id={self.id}, " + \
            f"make={self.make}, " + \
            f"model={self.model}, " + \
            f"licence_plate = {self.licence_plate}, " + \
            f"driver_id = {self.driver_id})"
                                        

class Driver_Review(Base):
    __tablename__ = 'driver_reviews'
    
    id = Column(Integer, primary_key=True)
    rating = Column(Integer)
    comment=Column(String)
    
    driver_id = Column(Integer, ForeignKey('drivers.id'))
    
    def __repr__(self):
        return f'Driver_Review(id={self.id}, ' + \
            f'rating={self.rating}, ' + \
            f'driver_id={self.driver_id})'