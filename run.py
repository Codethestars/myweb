from app import app
import os

print("Current working directory:", os.getcwd())

if __name__ == '__main__':
    app.run(debug=True)