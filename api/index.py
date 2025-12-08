import sys
import os

# Add parent directory to Python path so we can import the Flask app
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

# Import the Flask app from the root directory
from app import app

# Vercel's @vercel/python builder automatically detects the 'app' variable
# and uses it as the WSGI application handler for serverless functions
# The variable name 'app' is the standard convention for Flask apps on Vercel

