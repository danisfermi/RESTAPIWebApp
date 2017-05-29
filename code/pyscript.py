#!/usr/bin/python
import requests

cont = 'Yes'
while (cont=='yes' or cont=='Yes' or cont=='Y' or cont=='y' or cont=='YES'):
	print "Python Script to Interact with the REST API"
	print "-------------------------------------------"
	print "The following choices are available:-"
	print "1, GET Request to fetch all data"
	print "2. GET Request to fetch specific data"
	print "3. POST Request to insert a Contact"
	print "4. PUT Request to update a Contact"
	print "5. DELETE Request to delete a Contact"
	ch = raw_input("Enter your choice: ")
	if ch == '1':
		r = requests.get('http://127.0.0.1:5000/contacts')
		print "Response from the server in JSON"
		print r.json()
	elif ch == '2':
		id = raw_input("Enter the ID of the Contact you wish to fetch: ")
		payload = {'id':id}
		r = requests.get('http://127.0.0.1:5000/contact', params = payload)
		print "Response from the server in JSON"
		print r.json()
	elif ch == '3':
		name = raw_input("Enter the Name of the new Contact: ")
		mail = raw_input("Enter the Mail of the new Contact: ")
		r = requests.post('http://127.0.0.1:5000/contacts', data = {'name':name ,'mail':mail})
		print "Response Status from Server"
		print r.status_code
	elif ch == '4':
		id = raw_input("Enter the ID of the Contact you wish to update: ")
		name = raw_input("Enter the new Name of the Contact: ")
		mail = raw_input("Enter the new Mail of the Contact: ")
		url = 'http://127.0.0.1:5000/contacts/id='+id
		r = requests.put(url, json = {'name':name ,'mail':mail}).json()
		print "Check if Success using Option 1"
	elif ch == '5':
		id = raw_input("Enter the ID of the Contact you wish to delete: ")
		url = 'http://127.0.0.1:5000/contacts/id='+id
		r = requests.delete(url)
		print "Response Status from Server"
		print r.status_code
	else:
		print "Please Enter Valid Choice"
	cont = raw_input("Do you want to continue?: ")
