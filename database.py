from flask_sqlalchemy import SQLAlchemy
from enum import unique
import string
from sqlalchemy.orm import backref
from datetime import datetime 
import random 

db = SQLAlchemy()


class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.Text(), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())

    def __repr__(self) -> str:
        return 'User >>> {self.username}'


class CountryData(db.Model):
    country_id = db.Column(db.Integer, primary_key=True)
    country_name = db.Column(db.Text, nullable=True)
    energy_source = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())
    
    def __repr__(self):
        return f"Country Name('{self.country_name}')"



class Building(db.Model):
    building_no = db.Column(db.Integer, primary_key=True)
    width = db.Column(db.Integer, nullable=True)
    height = db.Column(db.Integer, nullable=True)
    type_of_land = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return f"Building Area is: '{self.building_no}'"


class Population(db.Model):
    pop_id = db.Column(db.Integer, primary_key=True)
    building_id = db.Column(db.Integer, nullable=True)
    p_count = db.Column(db.Integer, nullable=True)
    c_energy = db.Column(db.Float, nullable=True)
    r_energy = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return f"Population is {self.p_count}"


class SolarPanels(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    no_plates = db.Column(db.Integer, nullable=False)
    cost_panels = db.Column(db.Integer, nullable=False)
    estimated_profits = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"No of plates is: '{self.no_plates}'"


