import sys
import os

# Add the path to the HAEstates folder to the module search path
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')

from HAEstates import app

if __name__ == '__main__':
    app.run(debug=True)
