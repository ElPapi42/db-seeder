import os
import pathlib

from dotenv import load_dotenv


# Load .env vars
dotenv_path = pathlib.Path('.').parent/'.env'
load_dotenv(dotenv_path)

DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DB_USERNAME = os.environ.get('DB_USERNAME')
DB_PASSWORD = os.environ.get('DB_PASSWORD')

# Build the mongo url
DB_URL = f'mongodb://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}'