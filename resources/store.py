from flask_restful import Resource, reqparse
from models.store import StoreModel
from flask_jwt import jwt_required

class Store(Resource):

    @jwt_required()
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json(), 200
        return {"message":"Store of name '{}' does not exist in the system ".format(name)}, 400


    def post(self, name):
        store = StoreModel.find_by_name(name)
        if store is not None:
            return {"message":"Store of name '{}' exist in the system".format(name)}, 400
        
        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {"message":"Error occured while inserting data in the system"}, 500
        return store.json(), 201

    @jwt_required()
    def delete(self, name):
        if name is '' or None:
            return {"message":"Please enter the name of the store"}, 400
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
            return {"message":"Store of name '{}' is deleted from the system".format(name)}, 200
        else:
            return {"message":"Store of name '{}' does not exist in the system".format(name)}, 400

class StoreList(Resource):

    def get(self):
        return {"stores":[store.json() for store in StoreModel.query.all()]}
