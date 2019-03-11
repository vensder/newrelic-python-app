#!/usr/bin/env python3

from flask import Flask
app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return '<b>Welcome to %s admin page</b>\
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
  			<input type="submit" value="Submit">' % path

if __name__ == '__main__':
    app.run(host='0.0.0.0')
