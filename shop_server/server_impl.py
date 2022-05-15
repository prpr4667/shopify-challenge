import http

from shop_server import constants
from shop_server.Item import Item
import json
# holds the mapping between the name of the item and the object
from shop_server.status import Status

items = {}
# can be used to store the status of the item in the database
status = {}
# use the store datastore to maintain data about the items like quantity in the warehouse etc
store = {}

def createItem(name, category, keywords):
	response = {}
	item = Item(name, category, keywords)
	if name not in items:
		items[name] = item
		status[name] = Status()
		status[name].update_status(constants.INACTIVE, constants.NULL_COMMENT)
		response["message"] = "SUCCESS"
		return response, http.HTTPStatus.OK
	response["message"] = "ALREADY EXISTS"
	return response, http.HTTPStatus.CONFLICT

		
def updateItem(name, category, keywords):
	response = {}
	if name not in items:
		response["message"] = "DOES NOT EXIST"
		return response, http.HTTPStatus.CONFLICT
	item = items[name]
	item.update_item(category, keywords)
	items[name] = item
	response["message"] = "SUCCESS"
	return response, http.HTTPStatus.OK


# basic functionality to delete an item from the database
def deleteItem(name):
	response = {}
	if name not in items or name not in status:
		response["message"] = "DOES NOT EXIST"
		return response, http.HTTPStatus.CONFLICT
	del items[name]
	del status[name]
	response["message"] = "SUCCESS"
	return response, http.HTTPStatus.OK

	
# gives an option to delete an item using a flag to undelete it in the future if needed
def softDeleteItem(name, new_status, new_comment):
	response = {}
	if name not in items or name not in status:
		response["message"] = "DOES NOT EXIST"
		return response, http.HTTPStatus.CONFLICT
	item_status = status[name]
	item_status.update_status(new_status, new_comment)
	status[name] = item_status
	response["message"] = "SUCCESS"
	return response, http.HTTPStatus.OK
	
	
def viewItems():
	results = []
	for item in items:
		if item not in status:
			continue
		item_status = status[item]
		if item_status.get_status() is constants.PROMOTED:
			item_dict = items[item].__dict__
			item_dict["status"] = constants.status_text_mapping[item_status.get_status()]
			item_dict["comment"] = item_status.get_comment()
			# item_json = json.dumps(item_dict)
			results.insert(0, item_dict)
		if item_status.get_status() is constants.ACTIVE:
			item_dict = items[item].__dict__
			item_dict["status"] = constants.status_text_mapping[item_status.get_status()]
			item_dict["comment"] = item_status.get_comment()
			# item_json = json.dumps(item_dict)
			results.insert(len(results)-1, item_dict)
		if item_status.get_status() is constants.UNDER_MAINTENANCE:
			item_dict = items[item].__dict__
			item_dict["status"] = constants.status_text_mapping[item_status.get_status()]
			item_dict["comment"] = item_status.get_comment().upper()
			# item_json = json.dumps(item_dict)
			results.append(item_dict)
	return results, http.HTTPStatus.OK
			
			