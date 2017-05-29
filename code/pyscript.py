#!/usr/bin/python
import requests

cont = 'Yes'
while (cont=='yes' or cont=='Yes' or cont=='Y' or cont=='y' or cont=='YES'):
	print "Python Script to Interact with the REST API"
	print "-------------------------------------------"
	print "The following choices are available:-"
	print "1, GET Request to fetch all data"
	print "2. GET Request to fetch specific data"
	print "3. POST Request to insert a record"
	print "4. PUT Request to update a record"
	print "5. DELETE Request to delete a record"
	ch = raw_input("Enter your choice: ")
	if ch == '1':
		r = requests.get('http://127.0.0.1:5000/contacts')
		print "Response from the server in JSON"
		print r.json()
	elif ch == '2':
		id = raw_input("Enter the ID of the Record you wish to fetch: ")
		payload = {'id':id}
		r = requests.get('http://127.0.0.1:5000/contact', params = payload)
		print "Response from the server in JSON"
		print r.json()
	elif ch == '3':
		name = raw_input("Enter the Name of the new Record: ")
		mail = raw_input("Enter the Mail of the new Record: ")
		r = requests.post('http://127.0.0.1:5000/contacts', data = {'name':name ,'mail':mail})
		print "Response Status from Server"
		print r.status_code
	elif ch == '4':
		id = raw_input("Enter the ID of the Record you wish to update: ")
		name = raw_input("Enter the new Name of the Record. Else leave blank: ")
		mail = raw_input("Enter the new Mail of the Record. Else leave blank: ")
		url = 'http://127.0.0.1:5000/contacts/id='+id
		r = requests.put(url, data = {'name':name ,'mail':mail})
		print "Response Status from Server"
		print r.status_code
	elif ch == '5':
		id = raw_input("Enter the ID of the Record you wish to delete: ")
		url = 'http://127.0.0.1:5000/contacts/id='+id
		r = requests.delete(url)
		print "Response Status from Server"
		print r.status_code
	else:
		print "Please Enter Valid Choice"
	cont = raw_input("Do you want to continue?: ")
