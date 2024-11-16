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

# Data retrieval route for Plumbing page 2
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
