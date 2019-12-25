from flask import Flask,request
from flask_restful import Resource,Api,reqparse
#reqparse is used to only pass specific itmes through json payload
from flask_jwt import JWT,jwt_required

from security import authentication,identity

from resources.user import UserRegister

from resources.item import Item,Items

from resources.store import Store,StoreList

from db import db


app = Flask(__name__) #resource is just a thing you api can be mapped to that the subject of data
db.init_app(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = "kushal" #secrete key for api authentication

api = Api(app) #to handle the resources easily get,post etc

#we dont have to add jsonify with flask restful since it automatically does that so we can only pass dictionary


@app.before_first_request
def create_tables():
	db.create_all()

#uwsgi helps our flask app to interact with othe things

jwt = JWT(app,authentication,identity) #all three thing will be sed for the authentication of users 

api.add_resource(Items, '/items')

api.add_resource(Item, '/item/<string:name>')

api.add_resource(StoreList, '/stores')

api.add_resource(Store, '/store/<string:name>')

api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
	db.init_app(app)
	app.run(debug=True)
