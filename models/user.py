from database import db

class UserModel(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))
    
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def getPassword(self):
        return self.password

    def json(self):
        return {"username":self.username, "password":self.password}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def findUserById(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def findUserByUsername(cls, username):
        return cls.query.filter_by(username=username).first()

        