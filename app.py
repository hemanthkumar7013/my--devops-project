from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host=os.environ['DB_HOST'],
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASSWORD'],
        database=os.environ['DB_NAME']
    )

@app.route('/')
def home():
    return "Flask connected to RDS 🚀"

@app.route('/add')
def add_user():
    try:
        db = get_db_connection()
        cursor = db.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))")
        cursor.execute("INSERT INTO users (name) VALUES ('Hemanth')")
        db.commit()
        return "User added to RDS ✅"
    except Exception as e:
        return f"Error: {str(e)}"

@app.route('/users')
def users():
    try:
        db = get_db_connection()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users")
        result = cursor.fetchall()
        return str(result)
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
