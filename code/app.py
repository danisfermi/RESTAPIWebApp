#!/usr/bin/python
from flask import Flask
from flask import abort, make_response

app = Flask(__name__)

# Index
@app.route('/')
def index():
	return "Hello World"

# Base GET Request
@app.route('/contacts', methods = ['GET'])
def get_contacts():
	return jsonify({'contacts':contacts})

# Name Based Get Request
@app.route('/contacts/<string:name>', methods = ['GET'])
def get_contact(name):
	contact = [contact for contact in contacts if contact[name] == name]
	if len(contact) == 0:
		abort(404)
	return jsonify({'contact': contact})

# Error Handler to convert Error 404 to JSON
@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'Error':'Not Found'}),404)

# Memory Database
# JSON Formatted. Fields are:-
#			+Name (string)
# 			+Mail (string)
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
