from app import app
from db import db

db.init(app)

#this is because now we are running this app from uwsgi
#and now __name__ == '__main__': will not be executed 

#heroku login
#heroku logs

@app.before_first_request
def create_tables():
	db.create_all()

#this will create all the tables for us
