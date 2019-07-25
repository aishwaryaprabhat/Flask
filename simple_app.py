from flask import Flask 

app = Flask(__name__)

@app.route('/') #http://www.google.com/maps
def home(): #name of the function does not matter only the route matters
	return "Hello, World!"


app.run(port=5000)