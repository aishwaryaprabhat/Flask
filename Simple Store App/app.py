from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

stores = [
			{
			'name':"My wonderful store", 
			'items': [ 
						{'name':'My item', 'price':15.99}, 
					 ] 
			},
		]


@app.route("/")
def home():

	return render_template("index.html")

#Simple GET stores
@app.route("/stores")
def get_stores():
	
	return jsonify({'stores':stores})


#GET particular store 
@app.route("/stores/<string:name>")
def get_specific_store(name):
	
	for store in stores:
		if store['name']==name:
			return jsonify(store)
		else:
			continue
	return jsonify({'message':"Store does not exist"})


#GET items in store
@app.route("/stores/<string:name>/item")
def get_items(name):
	
	for store in stores:
		if store['name']==name:
			return jsonify({'items':store['items']})
		else:
			continue
	return jsonify({'message':"Store does not exist"})


#POST create store
@app.route("/stores",methods=['POST'])
def create_store():
	
	request_data = request.get_json()
	new_store = {
				'name':request_data['name'],
				'items':[]
				}
	stores.append(new_store)
	return jsonify(new_store)


#POST create item
@app.route("/stores/<string:name>/item")
def create_item(name):
	
	request_data = request.get_json()
	try:
		new_item = {'name':request_data['name'], 
					'price':request_data['price']}
		stores['name'].append(new_item)
		return jsonify({"item":new_item})
	except:
		return jsonify({"message":"Store does not exist"})


app.run()