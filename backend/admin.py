# Admin - this class inherits from User and adds extra methods for admins only
# Written by Alex Robbins

from backend.user import User
from backend.db_user import db

class Admin(User):

    def admin_add_user_to_db(self,user, admin_email):
        return self.our_db.admin_add_user_to_db(user,admin_email)

    def remove_user_from_db(self,email):
        return self.our_db.remove_user_from_db(email)

    def promote_to_admin(self,email):
        return self.our_db.promote_to_admin(email)

    def list_users(self):
        return self.our_db.list_users()
