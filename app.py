from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

db = mysql.connector.connect(
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
    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))")
    cursor.execute("INSERT INTO users (name) VALUES ('Hemanth')")
    db.commit()
    return "User added to RDS ✅"

@app.route('/users')
def users():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users")
    result = cursor.fetchall()
    return str(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)