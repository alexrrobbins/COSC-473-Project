# TODO: Add database code to perform these functions
class db():

    def add_user_to_db(user):
        # Add user to database
        print(user.get_username())
        print(user.get_email())
        return True

    def verify_credentials(user):
        #verify the user's credentials
        print(user.get_email())
        return True

    def change_password_in_db(user):
        #change the password in db
        return True

    def get_username(user):
        pass
