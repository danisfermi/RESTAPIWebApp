#!/usr/bin/python
import urllib2

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

