from flask import Flask, request
import mysql.connector
import os

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host=os.environ.get('DB_HOST'),
        user=os.environ.get('DB_USER'),
        password=os.environ.get('DB_PASSWORD'),
        database=os.environ.get('DB_NAME'),
        connection_timeout=5
    )

@app.route('/')
def home():
    return "Flask connected to RDS 🚀"

@app.route('/add')
def add_user():
    db = None
    cursor = None
    try:
        name = request.args.get('name', 'Hemanth')

        db = get_db_connection()
        cursor = db.cursor()

        cursor.execute("INSERT INTO users (name) VALUES (%s)", (name,))
        db.commit()

        return f"User {name} added to RDS ✅"

    except Exception as e:
        return f"Error: {str(e)}"

    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()

@app.route('/users')
def users():
    db = None
    cursor = None
    try:
        db = get_db_connection()
        cursor = db.cursor()

        cursor.execute("SELECT * FROM users")
        result = cursor.fetchall()

        return str(result)

    except Exception as e:
        return f"Error: {str(e)}"

    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
