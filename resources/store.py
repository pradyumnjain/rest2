from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):
	def get(self,name):
		store = StoreModel.find_by_name(name)
		if store:
			return store.json()
		return {'message':'store not found'},404

	def post(self,name):
		store = StoreModel.find_by_name(name)
		if store:
			return {'message':'store {} already exists'.format(name)}

		store = StoreModel(name)
		try:
			store.save_to_db()
		except:
			return {'message':'an error occured'}

		return store.json()

	def delete(self,name):
		store = StoreModel.find_by_name(name)
		if store:
			store.delete_from_db()
			return {'message':'store {} is deleted'.format(name)}
		return {'message':'store does not exists'}

class StoreList(Resource):
	def get(self):
		return {'stores':[store.json() for store in StoreModel.query.all()]}