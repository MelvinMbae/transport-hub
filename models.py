from sqlalchemy import create_engine
from sqlalchemy import (UniqueConstraint, Column, Integer, String, Float, Boolean, Date, ForeignKey)

from sqlalchemy.orm import relationship, backref


from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///transport_hub.db')

Base = declarative_base()

class Driver(Base):
    __tablename__ = 'drivers'
    __table_args__ = (
        UniqueConstraint('email', name='unique_email')
    )

    id = Column(Integer, primary_key=True)
    name=Column(String)
    gender=Column(String)
    date_of_birth=Column(Date)
    years_of_experience=Column(Integer)
    
    

class Car(Base):
    __tablename__ = 'cars'
    __table_args__ = (UniqueConstraint('licence_plate',name='unique_licence_plate'))
    
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