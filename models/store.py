from db import db

class StoreModel(db.Model):

	__tablename__ = 'store'

	id = db.Column(db.Integer , primary_key=True)
	name = db.Column(db.String(80))

	items = db.relationship('ItemModel',lazy='dynamic')#ccoz of lazy it will only be called when it is executed
	#mpas a store to its every item


	def __init__(self,name):
		self.name = name

	def json(self):
		return {'name':self.name ,'items': [item.json() for item in self.items.all()]}
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
