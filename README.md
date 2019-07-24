# REST API
Largely based on this [Udemy course](https://www.udemy.com/rest-api-flask-and-python/)
### What is a web server?
- Sometimes referred to the hardware
- Sometimes referred to a pieve of software designed to respond to a user request

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

