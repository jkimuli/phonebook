import os
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

app = Flask(__name__,static_folder="static/build")
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

# Loading environment variables

APP_ROOT = os.path.join(os.path.dirname(__file__), '..')   # refers to application_top
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)

app.config['aws_access_key'] = os.getenv('AWS_ACCESS_KEY')
app.config['aws_secret'] = os.getenv('AWS_SECRET_ACCESS_KEY')

from server import routes