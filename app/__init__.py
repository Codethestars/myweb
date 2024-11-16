from flask import Flask
import os

# Set up the base directory and template directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

print("Template directory:", TEMPLATE_DIR)  # Debugging line to check template directory path
print("Does template directory exist?", os.path.exists(TEMPLATE_DIR))  # Debugging to confirm existence
print("Template directory contents:", os.listdir(TEMPLATE_DIR))  # Debugging to list contents

# Initialize the Flask app
app = Flask(__name__,
            static_folder='static',
            static_url_path='/static',
            template_folder=TEMPLATE_DIR)

# Import the consolidated routes file (mroutes.py)
from app.routes import mroutes

# Ensure static directories are present (optional setup for static files)
static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
if not os.path.exists(static_dir):
    os.makedirs(static_dir)

# Ensure the CSS directory exists
css_dir = os.path.join(static_dir, 'css')
if not os.path.exists(css_dir):
    os.makedirs(css_dir)
