from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3
from models.item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help="This field cannot be left blank")
    parser.add_argument('store_id', type=int, required=True, help="Store id is essential for item to exist in the system")

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item is None:
            return {"Message":"This item is not present in the system"}, 400
        return {"item":item.json()}, 200

    def post(self, name):
        item = ItemModel.find_by_name(name)
        if item is not None:
            return {"Message":"Item of name'{}' exist in the system".format(name)},400
        
        data = Item.parser.parse_args()

        item = ItemModel(name, data['price'], data['store_id'])
        try:
            item.save_to_db()
        except:
            return {"Message":"Error in inserting the data inside the system"}

        return item.json(), 201

    @jwt_required()
    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
            return {"Message":"Item deleted"}
        else:
            return {"Message":"Invalid item"}

    def put(self, name):
        item = ItemModel.find_by_name(name)
        data = Item.parser.parse_args()
        if item is None:
            item = ItemModel(name, data['price'], data['store_id'])
        else:
            item.setPrice(data['price'])
        item.save_to_db()
        return item.json(), 201


class Items(Resource):
    def get(self):
        return {"items": list(map(lambda x: x.json(), ItemModel.query.all()))}
        # alternative of map method
        # [item.json() for item in ItemModel.query.all()]


        # Map method is used for applying changes to each element in the list
        # So we used it to convert each item object into json representation
        
        