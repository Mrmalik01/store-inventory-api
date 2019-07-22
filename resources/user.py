from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegistry(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="This field is required"
    )
    parser.add_argument('password',
        type=str,
        required=True,
        help="This field is required"
    )

    def post(self):
        data = UserRegistry.parser.parse_args()
        if UserModel.findUserByUsername(data['username']):
            return {"Message":"Username is being used by someone."}
        user = UserModel(**data) # copying all the key values from the data to the UserModel keys
        user.save_to_db() #
        return {"Message":"User with username ('{}') is created in the system".format(data['username'])}


