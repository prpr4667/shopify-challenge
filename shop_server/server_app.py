from flask import Flask, request, jsonify, Response

from shop_server.server_impl import *

app = Flask(__name__)


@app.route('/item/create', methods=['POST'])
def create_item():
	print(request)
	req = request.get_json()
	resp, status_code = createItem(req['name'], req['category'], req['keywords'])
	
	return resp, status_code


@app.route('/item/update', methods=['POST'])
def update_item():
	req = request.get_json()
	resp, status_code = updateItem(req['name'], req['category'], req['keywords'])
	
	return resp, status_code


@app.route('/item/delete', methods=['POST'])
def delete_item():
	req = request.get_json()
	resp, status_code = deleteItem(req['name'])
	return resp, status_code


@app.route('/item/toggle_delete', methods=['POST'])
def soft_delete_item():
	req = request.get_json()
	resp, status_code = softDeleteItem(req['name'], req['status'], req['comment'])
	return resp, status_code


@app.route('/item/fetch', methods=['GET'])
def view_items():
	resp, status_code = viewItems()
	return json.dumps(resp), status_code


if __name__ == '__main__':
	app.run()