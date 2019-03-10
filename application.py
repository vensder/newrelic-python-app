#!/usr/bin/env python3

from bottle import route, run, template

@route('/')
def start():
	return "Welcome to admin page"

@route('/<anything>')
def index(anything):
	return template('<b>{{anything}}</b>\
		</br>\
			You need the authorization to access this page\
		</br>\
		</br>\
		<form>\
	  		User name:<br>\
	  			<input type="text" name="username"><br>\
	  		User password:<br>\
	  			<input type="password" name="psw">\
		</form>\
  			<input type="submit" value="Submit">',
		anything=anything)

run(host='0.0.0.0', port=8080)

