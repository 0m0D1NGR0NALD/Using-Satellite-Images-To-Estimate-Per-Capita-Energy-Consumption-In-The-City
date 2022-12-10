from flask import Blueprint, request, jsonify

census_data = {

    'Freetown': {'population_size': '1,200,000', 
    'Energy Sources': 'BioMass, HydroPower, Solar'},

    'Mumbai': {'population_size': '24,200,000', 
    'Energy Sources': 'HydroPower, Solar'}
}


def country_data(name):
    data = census_data[name]
    return jsonify({})
