# TODO: Add database code to perform these functions

class db():

    def __init__(self):
        import mysql.connector as mysql
        # REALLY BAD PRACTICES FOR THE THE REAL WORLD RIGHT HERE
        # I MEAN I ACKNOWLEDGE THAT WE ARE LITERALLY DOING EVERYTHING WRONG HERE
        # BUT THIS IS FOR EDUCATIONAL PURPOSES ONLY SO IT'S FINE
        HOST = "sql5.freemysqlhosting.net"
        DATABASE = "sql5391708"
        USER = "sql5391708"
        PASSWORD = "9NzI7Gvk1W"
        self.db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)

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
