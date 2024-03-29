from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from security import authenticate, identity
from resources.user import UserRegistry
import sqlite3
from resources.item import Item, Items
from resources.store import Store, StoreList
import os

app = Flask(__name__)
app.secret_key = 'secret_code'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(Item, '/item/<string:name>')
api.add_resource(Items, '/items')
api.add_resource(UserRegistry, '/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList,'/stores')

if __name__ == '__main__':
    from database import db
    db.init_app(app)
    port = int(os.environ.get('PORT', 5000))
    app.run(port=port, debug=True)
    

        

