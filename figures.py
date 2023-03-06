from flask import Blueprint, request, jsonify
# Create dictionary with city population and available energy sources
census_data = {
    'Freetown': {'population_size': '1,200,000', 
    'Energy Sources': 'BioMass, HydroPower, Solar'},

    'Mumbai': {'population_size': '24,200,000', 
    'Energy Sources': 'HydroPower, Solar'}
}

def country_data(name):
    # Load items in dictionary with census data
    data = census_data[name]
    # Return conversion of dictionary to json file
    return jsonify({})
