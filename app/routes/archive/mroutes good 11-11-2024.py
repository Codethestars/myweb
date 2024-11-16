from flask import render_template, jsonify
from app import app
import os

# Index route
@app.route('/')
def index():
    """Route for the main index page"""
    return render_template('index.html')

# HVAC Landing page and related routes
@app.route('/landing')
def landing():
    """Route for the HVAC landing page"""
    return render_template('mlanding.html')

@app.route('/page1')
def page1():
    """Route for HVAC page 1"""
    return render_template('mpage1.html')

@app.route('/page2')
def page2():
    """Route for HVAC page 2"""
    return render_template('mpage2.html')

@app.route('/page3')
def page3():
    """Route for HVAC page 3"""
    return render_template('mpage3.html')

# Plumbing Landing page and related routes
@app.route('/planding')
def planding():
    """Route for the plumbing landing page"""
    return render_template('planding.html')

@app.route('/ppage1')
def ppage1():
    """Route for Plumbing page 1"""
    return render_template('ppage1.html')

@app.route('/ppage2')
def ppage2():
    """Route for Plumbing page 2"""
    return render_template('ppage2.html')

@app.route('/ppage3')
def ppage3():
    """Route for Plumbing page 3"""
    return render_template('ppage3.html')

@app.route('/ppage4')
def ppage4():
    """Route for Plumbing page 4"""
    return render_template('ppage4.html')

@app.route('/ppage5')
def ppage5():
    """Route for Plumbing page 5"""
    return render_template('ppage5.html')

@app.route('/ppage6')
def ppage6():
    """Route for Plumbing page 6"""
    return render_template('ppage6.html')

# Electrical Landing page and related routes
@app.route('/elanding')
def elanding():
    """Route for the electrical landing page"""
    return render_template('elanding.html')

@app.route('/epage1')
def epage1():
    """Route for Electrical page 1"""
    return render_template('epage1.html')

# Data retrieval routes for HVAC pages
@app.route('/get_data')
def get_data():
    """API route to fetch data from mpage1.txt"""
    data = []
    data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data', 'mpage1.txt')
    
    with open(data_path, 'r') as file:
        headers = file.readline().strip().split('|')
        for line in file:
            values = line.strip().split('|')
            data.append(dict(zip(headers, values)))
    return jsonify(data)

@app.route('/get_data_page2')
def get_data_page2():
    """API route to fetch data from mpage2.txt"""
    data = []
    data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data', 'mpage2.txt')
    
    with open(data_path, 'r') as file:
        headers = file.readline().strip().split('|')
        for line in file:
            values = line.strip().split('|')
            data.append(dict(zip(headers, values)))
    return jsonify(data)

@app.route('/get_data_page3')
def get_data_page3():
    """API route to fetch data from mpage3.txt"""
    data = []
    data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data', 'mpage3.txt')
    
    with open(data_path, 'r') as file:
        headers = file.readline().strip().split('|')
        for line in file:
            values = line.strip().split('|')
            data.append(dict(zip(headers, values)))
    return jsonify(data)

# Data retrieval routes for Plumbing pages
@app.route('/get_data_ppage1')
def get_data_ppage1():
    """API route to fetch data from ppage1.txt"""
    data = []
    data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data', 'ppage1.txt')
    
    with open(data_path, 'r') as file:
        headers = file.readline().strip().split('|')
        for line in file:
            values = line.strip().split('|')
            data.append(dict(zip(headers, values)))
    return jsonify(data)

@app.route('/get_data_ppage2')
def get_data_ppage2():
    """API route to fetch data from ppage2.txt"""
    data = []
    data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data', 'ppage2.txt')
    
    with open(data_path, 'r') as file:
        headers = file.readline().strip().split('|')
        for line in file:
            values = line.strip().split('|')
            data.append(dict(zip(headers, values)))
    return jsonify(data)

@app.route('/get_data_ppage3')
def get_data_ppage3():
    """API route to fetch data from ppage3.txt"""
    data = []
    data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data', 'ppage3.txt')
    
    with open(data_path, 'r') as file:
        headers = file.readline().strip().split('|')
        for line in file:
            values = line.strip().split('|')
            data.append(dict(zip(headers, values)))
    return jsonify(data)

@app.route('/get_data_ppage4')
def get_data_ppage4():
    """API route to fetch data from ppage4.txt"""
    data = []
    data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data', 'ppage4.txt')
    
    with open(data_path, 'r') as file:
        headers = file.readline().strip().split('|')
        for line in file:
            values = line.strip().split('|')
            data.append(dict(zip(headers, values)))
    return jsonify(data)

@app.route('/get_data_ppage5')
def get_data_ppage5():
    """API route to fetch data from ppage5.txt"""
    data = []
    data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data', 'ppage5.txt')
    
    with open(data_path, 'r') as file:
        headers = file.readline().strip().split('|')
        for line in file:
            values = line.strip().split('|')
            data.append(dict(zip(headers, values)))
    return jsonify(data)

@app.route('/get_data_ppage6')
def get_data_ppage6():
    """API route to fetch data from ppage6.txt"""
    data = []
    data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data', 'ppage6.txt')
    
    with open(data_path, 'r') as file:
        headers = file.readline().strip().split('|')
        for line in file:
            values = line.strip().split('|')
            data.append(dict(zip(headers, values)))
    return jsonify(data)

# Data retrieval routes for Electrical pages
@app.route('/get_data_epage1')
def get_data_epage1():
    """API route to fetch data from epage1.txt"""
    data = []
    data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data', 'epage1.txt')
    
    with open(data_path, 'r') as file:
        headers = file.readline().strip().split('|')
        for line in file:
            values = line.strip().split('|')
            data.append(dict(zip(headers, values)))
    return jsonify(data)