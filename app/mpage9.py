import os
from flask import jsonify, request

def read_data(filepath):
    data = []
    with open(filepath, 'r') as file:
        next(file)  # Skip header
        for line in file:
            values = line.strip().split('|')
            row = {
                'dry_bulb': float(values[0]),
                'rel_humidity': float(values[1]),
                'dew_point': float(values[2]),
                'wet_bulb': float(values[3]),
                'humidity_ratio': float(values[4]),
                'enthalpy': float(values[5]),
                'specific_volume': float(values[6])
            }
            data.append(row)
    return data

def get_unique_values():
    """Get unique values for dropdowns"""
    data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'mpage9.txt')
    data = read_data(data_path)
    
    dry_bulb_values = sorted(list(set(row['dry_bulb'] for row in data)))
    rel_humidity_values = sorted(list(set(row['rel_humidity'] for row in data)))
    
    return dry_bulb_values, rel_humidity_values

def find_matching_row(data, dry_bulb, rel_humidity):
    for row in data:
        if row['dry_bulb'] == dry_bulb and row['rel_humidity'] == rel_humidity:
            return row
    return None

DATA_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'mpage9.txt')
psychrometric_data = read_data(DATA_PATH)

def calculate_psychrometric():
    try:
        dry_bulb = float(request.form['dry_bulb'])
        rel_humidity = float(request.form['rel_humidity'])
        
        result = find_matching_row(psychrometric_data, dry_bulb, rel_humidity)
        
        if result:
            return jsonify({
                'success': True,
                'data': result
            })
        else:
            return jsonify({
                'error': 'No matching data found for the given inputs'
            })
            
    except ValueError:
        return jsonify({
            'error': 'Please enter valid numbers'
        })

def get_available_values():
    """Route to get available values for dropdowns"""
    dry_bulb_values, rel_humidity_values = get_unique_values()
    return jsonify({
        'dry_bulb_values': dry_bulb_values,
        'rel_humidity_values': rel_humidity_values
    })