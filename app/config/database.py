import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv('DB_URL')

def get_db_connection():
    return psycopg2.connect(DATABASE_URL)