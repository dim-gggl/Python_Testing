import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')

CLUBS_FILE = 'data/clubs.json'
COMPETITIONS_FILE = 'data/competitions.json'
