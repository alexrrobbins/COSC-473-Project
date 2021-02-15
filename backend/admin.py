from backend.user import User
from backend.db_user import db

class Admin(User):

    def remove_user_from_db(self,user):
        return self.our_db.remove_user_from_db(user)

    def promote_to_admin(self,user):
        pass
