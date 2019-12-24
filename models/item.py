import sqlite3
from db import db

class ItemModel(db.Model):

	__tablename__ = 'items'

	id = db.Column(db.Integer , primary_key=True)
	name = db.Column(db.String(80))
	price = db.Column(db.Float(precision=2))

	store_id = db.Column(db.Integer , db.ForeignKey('store.id'))

	store = db.relationship('StoreModel')#maps the item to the respective store 
	#in the storemodel table

	def __init__(self,name,price,store_id):
		self.name = name
		self.price = price
		self.store_id = store_id

	def json(self):
		return {'name':self.name ,'price':self.price}
		#we will still use a class method in this since we have to return a class object 
		#through this funtion as opposed to a dictionary
	@classmethod
	def find_by_name(cls,name):
		return cls.query.filter_by(name=name).first()
		#return items model object representing the data

#since we have made a class with the instances variable we dont need a classmethod

	def save_to_db(self):
		db.session.add(self)
		db.session.commit()
	

	
	def delete_from_db(self):
		db.session.delete(self)
		db.session.commit()
