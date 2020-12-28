from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db' # can be any SQL db like mysql, psql
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'andrei'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all() # this will create data.db

jwt = JWT(app, authenticate, identity) # /auth 

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')

if __name__ == "__main__":
    db.init_app(app) # register sqlalchemy extenion to the current app
    app.run(port=4999, debug=True)
