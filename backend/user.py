# User: this class stores user info and communicates between main app and database Logic
# Written by Alex Robbins
# Closed 2/8/2021

from backend.db_user import db

class User():

    def __init__(self, email, password, username='null', admin='null'):
        self.email = email
        self.password = password
        self.username = username
        self.admin = admin
        self.our_db = db()

# Getters - return strings, setter returns nothing

    def get_username(self):
        return self.username

    def get_email(self):
        return self.email

    def set_username(self):
        self.username = self.our_db.get_username(self)

# These functions return true or false based on whether the db actions were successful

    def change_password(self, new_password):
        pw_change_result = self.our_db.change_password_in_db(self.email, new_password)
        if pw_change_result:
            self.password = new_password
        return pw_change_result

    def add_to_db(self):
        return self.our_db.add_user_to_db(self)

    def verify_credentials(self):
        return self.our_db.verify_credentials(self)

    def check_admin_status(self):
        return self.our_db.check_admin_status(self)
