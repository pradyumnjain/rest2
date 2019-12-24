from flask import Flask,request
from flask_restful import Resource,reqparse
#reqparse is used to only pass specific itmes through json payload
from flask_jwt import JWT,jwt_required

import sqlite3

from models.item import ItemModel

class Item(Resource): #will inherit from class resource
	parser = reqparse.RequestParser()
	parser.add_argument('price',
		type=float,
		required=True,
		help='cant be blank')
	parser.add_argument('store_id',
		type=int,
		required=True,
		help='every item needs a store id')
	

	@jwt_required()
	def get(self,name):
		item = ItemModel.find_by_name(name)
		if item:
			return item.json() #since this is now an object and we cannot returnb an object
			#so we retrun this function from the model
		return {'message':'item not found'},404
	
	

	def post(self,name):
		item = ItemModel.find_by_name(name)
		if item:
			return {'message': "an item with the {} already exists".format(name)},400
		data = Item.parser.parse_args()
		#this will convert the type to json
		#silent = true if client does not want to pass json this wil simplty return a null instead of an error	
		
		item = ItemModel(name,data['price'],data['store_id'])
		try:
			item.save_to_db()
		except:
			return {'message':'an error ocurred while inserting'},500

		return item.json(),201

	def delete(self,name):
		item = ItemModel.find_by_name(name)
		if item:
			item.delete_from_db()

		return {'message':'item deleted'}


	def put(self, name):
		data = Item.parser.parse_args()

		item = ItemModel.find_by_name(name)

		if item is None:
			item = ItemModel(name,data['price'],data['store_id'])
		else:
			item.price = data['price']
			item.store_id = data['store_id']

		item.save_to_db()

		return item.json()

class Items(Resource): #will inherit from class resource
	def get(self):
		return {'items':[item.json() for item in ItemModel.query.all()]}
		#{'items':list(map(lambda x:x.json(),ItemModel.query().all()))}



		
