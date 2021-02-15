from backend.user import User
from backend.db_user import db

class Admin(User):

    def __init__(self):
        self.our_db = db()

    def add_user_to_db(self,email,password,username):
        new_user = User(email,password,username)
        return self.our_db.add_user_to_db(new_user)

    
