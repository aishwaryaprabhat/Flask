# REST API 
Largely based on this [Udemy course](https://www.udemy.com/rest-api-flask-and-python/)
### What is a web server?
- Sometimes referred to the hardware
- Sometimes referred to a piece of software designed to respond to a user request

### What is a request?
A request is data that a user/web app sends to a web server

```
GET /HTTP/1.1
Host www.google.com
```

### What are some ways in which a server might respond to a request?
- Error
- HTML code
- Some processed output
- Nothing 

### In what cases might a web server throw an error?
- If it does not support HTTP (eg: an SMTP server)
- If path not found (404)
- If server is unavailable

### Give an example of what a request looks like when you request a web page
When you access https://twitter.com/login

```
GET /login HTTP/1.1
Host: https://twitter.com 
```

### What are the different HTTP verbs and their meanings?
|Verb|Meaning|Example
---|---|---
GET|(User) Retrieve something|GET /login
POST|(Server) Receive data and use it|POST /item {'name':'chair','price':9.99}
PUT|Makes sure that there is something. If there isn't anything it will create|PUT /item {'name':'chair','price':9.99}
DELETE| Remove something| DELETE /item/1

### What is REST?
- Its a way of thinking/designing how a web server responds to a user's requests
- Two main characteristics:
	- Web server doesn't respond with data, responds with resources instead
	- Interactions are stateless

### What are resources in REST?
Resources are basically abstractions that encapsulate data. Its a way of thinking about data and how the server and user use it for interaction. `GET /item/chair` is retrieving the chair resource

### Give an example to explain what is meant by stateless in REST?
- A user logs into web application
- Server does not keep track of requests and responses related to the login and thus does not know that the user is logged in
- The web application must send enough data to identify the user in every request or else the server won't associate the request with the user
- In the same way, the server must be programmed to associate every request to the specific user 

### Flask Coding Conventions, Tips & Tricks
##### POST Request
```
from flask import Flask

app = Flask(__name__)

@app.route('/store',methods=['POST'])
def some_function():
	pass
```

#### GET Request
```
from flask import Flask

app = Flask(__name__)

@app.route('/store') #default is GET
def some_function():
	pass
```

#### POST Request with argument
```
from flask import Flask

app = Flask(__name__)

@app.route('/store/<string: name>/item',methods=['POST'])
def some_function(name):
	pass
```

#### Returning data using JSONify
jsonify is required to convert Python dictionary into a json object that can be read by JavaScript 

```
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/store/<string: name>/item',methods=['POST'])
def some_function(name):
	some_python_dicitonary = {....}
	return jsonify(some_python_dicitonary)

```

#### Receiving input data using Request
```
from flask import Flask, jsonify, request

app = Flask(__name__)

old_data =[{...},{...},{...}]
@app.route('/store/<string: name>/item',methods=['POST'])
def some_function(name):
	request_data = request.get_json() #converts json to dictionary
	new_data = {
				'key1':request_data['key1']
				'key2':request_data['key2']
				}
	old_data.ppend(new_data)
	return jsonify(new_data)

```

#### Testing your API
- [Using curl to test REST API app](https://www.baeldung.com/curl-rest)
- [Using Postman](https://www.guru99.com/postman-tutorial.html)











