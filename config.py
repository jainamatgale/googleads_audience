import os
from dotenv import load_dotenv
import pymysql

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")

# Database connection
def get_db_connection():
    return pymysql.connect(
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT")),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        cursorclass=pymysql.cursors.DictCursor
    )

# Email config
MAIL_CONFIG = {
    "MAIL_SERVER": os.getenv("MAIL_SERVER"),
    "MAIL_PORT": int(os.getenv("MAIL_PORT")),
    "MAIL_USE_TLS": os.getenv("MAIL_USE_TLS") == "True",
    "MAIL_USERNAME": os.getenv("MAIL_USERNAME"),
    "MAIL_PASSWORD": os.getenv("MAIL_PASSWORD")
}