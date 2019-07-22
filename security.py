from werkzeug.security import safe_str_cmp
from models.user import UserModel

def authenticate(username, password):
    user = UserModel.findUserByUsername(username)
    if user and safe_str_cmp(user.getPassword(),password):
        return user

def identity(payload):
    userid = payload['identity']
    return UserModel.findUserById(userid)