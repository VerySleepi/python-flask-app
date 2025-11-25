import os
import json
import mysql.connector
from config import db_config
from flask import render_template, current_app
from . import main

@main.route('/')
def index():
    return render_template('index.html', name='World')

@main.route('/about')
def about():
    return render_template('about.html', title='About', description='This is a simple Flask web app.')

@main.route('/fruits')
def fruits():
    fruit_list  = ["apple", "banana", "cherry", "date", "elderberry"]
    return render_template('fruits.html', title='List Example', fruits = fruit_list)

@main.route('/profile')
def show_profile():
    user = {"name": "Alice", "age": 30}
    return render_template("profile.html", title='Dictionary Example', user=user)

@main.route('/db_data')
def db_data():
    # Establish database connection
    conn = mysql.connector.connect(**db_config)
    
    # Create a cursor that returns results as dictionaries
    cursor = conn.cursor(dictionary=True)
    
    # Execute SQL query
    cursor.execute("SELECT * FROM staff")
    
    # Fetch all rows from the query result
    data = cursor.fetchall()
    
    # Clean up resources
    cursor.close()
    conn.close()
    
    # Pass data to template
    return render_template('db_data.html', data=data)

@main.route('/staffdata')
def staffdata():
    json_path = os.path.join(current_app.static_folder, 'data/staff.json')
    with open(json_path) as f:
        staff_data = json.load(f)
    return render_template('from_json.html', staffData=staff_data)

