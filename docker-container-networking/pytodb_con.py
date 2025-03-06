from flask import Flask, request, jsonify
import psycopg2
import pandas as pd
import os

# Initialize the Flask application
app = Flask(__name__)

data = []

postgre_connect = os.getenv('postgre_connect')
postgre_user = os.getenv('postgre_user')
postgre_password = os.getenv('postgre_password')

def connect_db():
    global conn
    try:
        conn = psycopg2.connect(
            host=postgre_connect,
            #host="host.docker.internal", using this we will be able to connect to postgressql running on local machine 
            # whereas we are providing ip of docker container and trying to connect to db running in a container
            database="postgres",
            password="admin",
            user="postgres",
            port="5432",
        )
        print("Database connection successful")
    except Exception as e:
        print(f"Error connecting to the database: {e}")

@app.route('/api/data', methods=['GET'])
def get_data():
    try:
        cursor = conn.cursor()
        cursor.execute("select * from office.employee e")
        data = cursor.fetchall()
    except Exception as e:
        print(f"Error getting data from the database: {e}")
    finally:
        cursor.close()
    return jsonify(data),200

@app.route('/api/data', methods=['POST'])
def post_data():
    new_data = request.get_json()
    insert_query = "insert into office.employee (first_name, last_name, hire_date, salary) values (%s, %s, %s, %s)"
    try:
        cursor = conn.cursor()
        cursor.execute(insert_query, (new_data['first_name'], new_data['last_name'], new_data['hire_date'], new_data['salary']))
        conn.commit()
    except Exception as e:      
        print(f"Error inserting data into the database: {e}")   
    finally:
        cursor.close()

    if not new_data:
        return jsonify({'error': 'No data provided'}),400
    
    data.append(new_data)
    return jsonify(data)

if __name__ == '__main__':
    connect_db()
    app.run(host = "0.0.0.0", port = "3000", debug=True)