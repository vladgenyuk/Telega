from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.environ.get('BOT_TOKEN')
BOT_NAME = os.environ.get('VladLeb_Bot')
ADMIN_ID = os.environ.get('ADMIN_ID')
ADMIN_FIRST_NAME = os.environ.get('ADMIN_FIRST_NAME')

DB_HOST = os.environ.get('DB_HOST')
DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASS')
DB_NAME = os.environ.get('DB_NAME')
DB_PORT = os.environ.get('DB_PORT')
