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
	return jsonify({'Contacts': contacts})

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
	if request.json and 'name' in request.json: # Handler for request in JSON format
		contact = {
			'id'  : contacts[-1]['id'] + 1,
			'name': request.json['name'],
			'mail': request.json['mail']
		}
	else:                                       # Handler for form based PUT Request
		contact = {
				'id'  : contacts[-1]['id'] + 1,
				'name': request.form['name'],
				'mail': request.form['mail']
			}
	contacts.append(contact)
	return jsonify({'Contact': contact}), 201

# PUT Request
@app.route('/contacts/<int:id>', methods=['PUT'])
def update_contact(id):
	contact = [contact for contact in contacts if contact['id'] == id]
	if len(contact) == 0:
		abort(404)
	if request.json:                           # Handler for JSON PUT Request  
		contact[0]['name'] = request.json.get('name',contact[0]['name'])
		contact[0]['mail'] = request.json.get('mail',contact[0]['mail'])
	return jsonify({'Contact': contact[0]})

# DELETE Request
@app.route('/contacts/<int:id>', methods=['DELETE'])
def delete_contact(id):
	contact = [contact for contact in contacts if contact['id'] == id]
	if len(contact) == 0:
		abort(404)
	contacts.remove(contact[0])
	return jsonify({'Result': True})

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
