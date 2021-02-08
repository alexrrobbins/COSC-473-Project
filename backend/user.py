# User: this class stores user info and communicates between main app and database Logic
# Written by Alex Robbins
# Closed 2/8/2021

##########This class is closed!!!##########
########Handle all logic in db_user file########
from backend.db_user import db

class User():

    def __init__(self, email, password, username):
        self.email = email
        self.password = password
        self.username = username

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def get_username(self):
        return self.username

    def get_email(self):
        return self.email

# These functions return true or false based on whether the db actions were successful
    def change_password(self, new_password):
        self.password = new_password
        return db.change_password_in_db(self)

    def add_to_db(self):
        return db.add_user_to_db(self)

    def verify_credentials(self):
        return db.verify_credentials(self)
