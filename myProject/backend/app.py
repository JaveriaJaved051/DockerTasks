from flask import Flask, jsonify
import os
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

# Function to establish connection to PostgreSQL
def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST", "database"),  # Default to 'database' as in Docker Compose service name
        database=os.getenv("POSTGRES_DB", "mydatabase"),
        user=os.getenv("POSTGRES_USER", "myuser"),
        password=os.getenv("POSTGRES_PASSWORD", "mypassword")
    )
    return conn

@app.route('/')
def index():
    try:
        # Connect to PostgreSQL and execute a query
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute('SELECT version()')
        db_version = cur.fetchone()

        # Fetch some data from the 'users' table (optional)
        cur.execute('SELECT * FROM users')
        users = cur.fetchall()

        cur.close()
        conn.close()

        return jsonify({
            "PostgreSQL Version": db_version,
            "Users": users  # Return the data from 'users' table
        })
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    # Run the Flask app on 0.0.0.0 to be accessible from other containers
    app.run(host='0.0.0.0', port=5000)
