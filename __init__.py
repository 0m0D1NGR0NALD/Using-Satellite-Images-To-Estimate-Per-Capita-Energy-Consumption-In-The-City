from flask import Flask, jsonify, render_template
import os
from src.auth import auth 
from src.database import db
from flask_jwt_extended import JWTManager
import torch
import pandas as pd 
from flask_cors import CORS



def create_app(test_config=None):

    app = Flask(__name__, 
    instance_relative_config=True)
    CORS(app)
    infeerence = 3458
    if test_config is None: 
        app.config.from_mapping(
            SECRET_KEY=os.environ.get("SECRET_KEY"),
            SQLALCHEMY_DATABASE_URI=os.environ.get("SQLALCHEMY_DB_URI"),
            SQLALCHEMY_TRACK_MODIFICATIONS=False,
            JWT_SECRET_KEY=os.environ.get('JWT_SECRET_KEY'),
        )

    else:
        app.config.from_mapping(test_config)

    
    @app.get("/")
    def index():
        return "Hello world"

    
    image_path = 'mumbai.png'
    
    def inference():
        model = torch.hub.load('ultralytics/yolov5', 'custom', 'best.pt')
        results = model('mumbai.png')
        max_width = results.xyxy[0][0][2]
        max_height = results.xyxy[0][0][3]
        max_area = max_width * max_height
        return {results}

    

    mumbai_population_2019 = 20185000
    domestic_consumption_2019 = 26996
    commercial_consumption_2019 = 10282
    industrial_consumption_2019 = 36028
    total_consumption_2019 = domestic_consumption_2019 + industrial_consumption_2019 + commercial_consumption_2019
 


    def energy_for_one_person(population, total_energy):
        energy_per_person = total_energy/population

        return energy_per_person


    Area = infeerence

    def intensity_of_area(energy_per_person, area, no_of_floors):
        x = energy_per_person * area 
        total_energy_intensity = x * no_of_floors
        return total_energy_intensity

    def percentage_of_total_energy(energy):
        ratio = energy / total_consumption_2019

        return ratio * 100


    @app.get("/dashboard")
    def dashb():
        Area = infeerence
        floors = 1 # number of floors for a bungalow 

        mumbai_population_2019 = 20185000
        domestic_consumption_2019 = 26996
        commercial_consumption_2019 = 10282
        industrial_consumption_2019 = 36028

        e_per_person = energy_for_one_person(mumbai_population_2019, domestic_consumption_2019)
        i_of_area = intensity_of_area(e_per_person, Area, floors)

        percentage_of_domestic = percentage_of_total_energy(domestic_consumption_2019)
        percentage_of_commercial = percentage_of_total_energy(commercial_consumption_2019)
        percentage_of_industrial = percentage_of_total_energy(industrial_consumption_2019)
        
    

        # SUGGESTIONS
        if Area > 100000 & int(i_of_area) < 5 : 
            suggestion1 = "We can install solar panels in the area which will lead to decrease energy intensity"

            suggestion2 = "Energy producing industries in high intensity areas can relocate here"

        elif Area < 100000 & int(i_of_area) > 5: 
            suggestions1 = "Energy producing companies should relocate to places with lower intensity"

            suggestions2 = "residents should reduce minimize use of energy consuming sources"

        else: 
            suggestion1, suggestion2 = "Stable Energy"


     

        return jsonify({'Area': Area, 'mumbai_pop': mumbai_population_2019, 
                    'domestic_consumption': domestic_consumption_2019, 'comm_consumption': commercial_consumption_2019,
                    'industrial_consumption': industrial_consumption_2019, 
                    'energy_intensity': i_of_area, 'percentage_of_domestic': percentage_of_domestic, 'percentage_of_commercial': percentage_of_commercial, 
                    'percentage_of_industrial': percentage_of_industrial, 
                    'suggestions': {'suggestion1': suggestion1, 'suggestion2': suggestion2}})

    db.app = app
    db.init_app(app)
     
    JWTManager(app)
    # app.register_blueprint(status_codes)
    app.register_blueprint(auth)
    # app.register_blueprint(bookmarks)
   

    return app 

