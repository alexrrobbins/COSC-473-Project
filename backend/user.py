from backend.db_sign_up import db

class User():

    def __init__(self, email, password, username):
        self.email = email
        self.password = password
        self.username = username

    def get_username(self):
        return self.username

    def get_email(self):
        return self.email

    def change_password(self, new_password):
        self.password = new_password
        db.change_password_in_db(self)

    def add_to_db(self):
        db.add_user_to_db(self)
