from flask import Flask
from config import get_db_connection

app = Flask(__name__)

@app.route('/')
def home():
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute("SELECT VERSION() AS version")
        version = cursor.fetchone()
    conn.close()
    return f"MySQL Connected! Version: {version['version']}"

if __name__ == '__main__':
    app.run(debug=True)
