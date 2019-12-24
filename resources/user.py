import sqlite3#to give the class ability to interact with the database
from flask_restful import Resource,reqparse
from flask import request
from models.user import UserModel

class UserRegister(Resource):

	parser = reqparse.RequestParser()
	parser.add_argument('username',
		type=str,
		required=True,
		help='cant be blank')

	parser.add_argument('password',
		type=str,
		required=True,
		help='cant be blank')

	def post(self):
		data = UserRegister.parser.parse_args() #got back the data from json pay load

		if UserModel.find_by_username(data['username']):
			return {'message':'user already exists'} ,400

		# user = UserModel(data['username'],data['password'])
		#same as
		user = UserModel(**data)
		user.save_to_db()

		return {'message':"user created successfully"},201 