#!/usr/bin/python
from flask import Flask, abort

app = Flask(__name__)

# Index
@app.route('/')
def index():
	return "Hello World"

# Base GET Request
@app.route('/contacts', methods = ['GET'])
def get_contacts():
	return jsonify({'contacts':contacts})

# Nmae Based Get Request
@app.route('/contacts/<string:name>', methods = ['GET'])
def get_contact(name):
	contact = [contact for contact in contacts if contact[name] == name]
	if len(contact) == 0:
		abort(404)
	return jsonify({'contact': contact})

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
