#!/usr/bin/python
from flask import Flask
from flask import jsonify
from flask import request
from flask import make_response
from flask import abort

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
@app.route('/contacts/<int:id>', methods = ['GET'])
def get_contact(id):
	contact = [contact for contact in contacts if contact['id'] == id]
	if len(contact) == 0:
		abort(404)
	return jsonify({'Contact': contact})

# Post Request
@app.route('/contacts', methods=['POST'])
def create_contact():
	contact = {
						'id'  : request.form['id'],
						'name': request.form['name'],
						'mail': request.form['mail']
						}
	contacts.append(contact)
	return jsonify({'Contact': contact}), 201

# Error Handler to convert Error 404 to JSON
@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'Error':'Not Found'}),404)

# Memory Database
# JSON Formatted. Fields are:-
#			+Id (int)
#			+Name (string)
# 			+Mail (string)
contacts = [
		{
			'id'  :  1, 
			'name': 'Danis',
			'mail': 'dfermi@ncsu.edu'
		},
		{
			'id'  :  2,
			'name': 'Rohit',
			'mail': 'rnambis@ncsu.edu'
		}
	]

if __name__ == '__main__':
	app.run(debug=True)
