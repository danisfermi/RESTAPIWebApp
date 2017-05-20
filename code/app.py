#!/usr/bin/python
from flask import Flask

app = Flask(__name__)

# Index
@app.route('/')
def index():
	return "Hello World"

# Base GET Request
@app.route('/contacts', method=['GET'])
def get_contacts():
	return jsonify({'contacts':contacts})

# Memory Database
# JSON Formatted. Fields are:-
#					+Name (string)
# 				+Mail (string)
contacts = [
							{
								'name': 'Danis',
								'mail': 'dfermi@ncsu.edu'
							},
							{
								'name': 'Rohit',
								'mail': 'rnambis@ncsu.edu'
							}
						]

if __name__ == '__main__':
	app.run(debug=True)
