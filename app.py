# from flask import Flask, render_template, request, jsonify
# import pymysql 
# from flask_cors import CORS  # Import CORS
# from flask_bcrypt import Bcrypt

# app = Flask(__name__)
# CORS(app)  # Enable CORS for all routes
# bcrypt = Bcrypt(app)

# # # Database Configuration
# # db = pymysql.connect(
# #     host="localhost",
# #     user="root",  # Change to your MySQL username
# #     password="MySQL@Secure!123",  # Change to your MySQL password
# #     database="user_db"
# # )

# def get_db_connection():
#     return pymysql.connect(
#         host="localhost",
#         user="root",  
#         password="MySQL@Secure!123",
#         database="user_db",
#         cursorclass=pymysql.cursors.DictCursor
#     )
# db = get_db_connection()
# cursor = db.cursor()

# # Route to Handle Form Submission
# @app.route('/register', methods=['POST'])
# def register():
#     if not request.is_json:
#         return jsonify({'message': 'Invalid request format. Expected JSON.'}), 400

#     data = request.json
    
#     try:
#         # Extract user input
#         first_name = data.get('firstName')
#         middle_name = data.get('middleName', '')
#         last_name = data.get('lastName')
#         email = data.get('email')
#         username = data.get('username')
#         password = data.get('password')
#         hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
#         gender = data.get('gender')
#         contact = data.get('contact')
#         security_key = data.get('securityKey')
#         city = data.get('city')

    
#         sql = """
#         INSERT INTO users (first_name, middle_name, last_name, email, username, password, gender, contact, security_key, city) 
#         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
#         """
#         connection = get_db_connection()  # Get a new DB connection
#         with connection.cursor() as cursor:
#             cursor.execute(sql, (first_name, middle_name, last_name, email, username,hashed_password, gender, contact, security_key, city))
#             connection.commit()
#         connection.close()

#         return jsonify({'message': 'Registration successful!'}), 201
#     except Exception as e:
#         connection.rollback()
#         connection.close()
#         return jsonify({'message': 'Error: ' + str(e)}), 400
    
#     finally:
#         if 'connection' in locals():
#             connection.close()

# if __name__ == '__main__':
#     print(app.url_map)
#     app.run(debug=True, port=5000)  # Ensure the port matches the frontend request






















# from flask import Flask, request, jsonify,render_template
# import mysql.connector
# from flask_cors import CORS  
# from flask_bcrypt import Bcrypt

# app = Flask(__name__)
# CORS(app)  
# bcrypt = Bcrypt(app)

# def get_db_connection():
#     return mysql.connect(
#         host="localhost",
#         user="root",  
#         password="MySQL@Secure!123",
#         database="user_db",
#         cursorclass=mysql.cursors.DictCursor
#     )
# @app.route('/')
# def index():
#     return render_template("index.html")

# # Route to Handle Form Submission
# @app.route('/add-data', methods=['POST'])
# def add_data():
#     if not request.is_json:
#         return jsonify({'message': 'Invalid request format. Expected JSON.'}), 400

#     data = request.json

#     conn = mysql.connect("user_db.db")
#     cursor = conn.cursor()
#     try:
#         # Extract user input
#         first_name = data.get('firstName')
#         middle_name = data.get('middleName', '')
#         last_name = data.get('lastName')
#         email = data.get('email')
#         username = data.get('username')
#         password = data.get('password')
#         hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
#         gender = data.get('gender')
#         contact = data.get('contact')
#         security_key = data.get('securityKey')
#         city = data.get('city')

#         sql = """
#         INSERT INTO users (first_name, middle_name, last_name, email, username, password, gender, contact, security_key, city) 
#         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
#         """
#         connection = get_db_connection()  
#         with connection.cursor() as cursor:
#             cursor.execute(sql, (first_name, middle_name, last_name, email, username, hashed_password, gender, contact, security_key, city))
#             connection.commit()
#         return jsonify({'message': 'Registration successful!'}), 201

#     except Exception as e:
#         if 'connection' in locals():
#             connection.rollback()
#         return jsonify({'message': 'Error: ' + str(e)}), 400

#     finally:
#         if 'connection' in locals():
#             connection.close()
# pass

# if __name__ == '_main_':
#     print(app.url_map)
#     app.run(debug=True, port=5000)






from flask import Flask, request, jsonify, render_template
import json
import os
import mysql.connector
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from config import DB_CONFIG

app = Flask(__name__)
CORS(app)
bcrypt = Bcrypt(app)

# JSON file path
JSON_FILE = os.path.join(os.getcwd(), "data", "users.json")

# Database Connection
def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

# Home route
@app.route('/')
def index():
    return render_template("register.html")

# Function to save user data to a JSON file
def save_user_to_file(user_data):
    try:
        if os.path.exists(JSON_FILE):
            with open(JSON_FILE, "r") as file:
                users = json.load(file)
        else:
            users = []

        users.append(user_data)

        with open(JSON_FILE, "w") as file:
            json.dump(users, file, indent=4)

    except Exception as e:
        print("Error saving data:", e)

# Route to handle registration
@app.route('/add-data', methods=['POST'])
def add_data():
    if not request.is_json:
        return jsonify({'message': 'Invalid request format. Expected JSON.'}), 400

    data = request.json
    try:
        first_name = data.get('firstName')
        middle_name = data.get('middleName', '')
        last_name = data.get('lastName')
        email = data.get('email')
        username = data.get('username')
        password = data.get('password')
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        gender = data.get('gender')
        contact = data.get('contact')
        security_key = data.get('securityKey')
        city = data.get('city')

        # Save user data to JSON file (optional)
        user_data = {
            "first_name": first_name,
            "middle_name": middle_name,
            "last_name": last_name,
            "email": email,
            "username": username,
            "password": hashed_password,
            "gender": gender,
            "contact": contact,
            "security_key": security_key,
            "city": city
        }
        save_user_to_file(user_data)

        # Save user to the database
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = """
        INSERT INTO users (first_name, middle_name, last_name, email, username, password, gender, contact, security_key, city) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (first_name, middle_name, last_name, email, username, hashed_password, gender, contact, security_key, city))
        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({'message': 'Registration successful!'}), 201

    except Exception as e:
        return jsonify({'message': 'Error: ' + str(e)}), 400

# Admin route to view registered users from file
@app.route('/view-users', methods=['GET'])
def view_users():
    if not os.path.exists(JSON_FILE):
        return jsonify({'message': 'No users registered yet.'}), 404

    with open(JSON_FILE, "r") as file:
        users = json.load(file)
    
    return jsonify(users), 200

@app.route("/")
def register():
    return render_template("register.html")

if __name__ == '__main__':
    app.run(debug=True, port=5000)
