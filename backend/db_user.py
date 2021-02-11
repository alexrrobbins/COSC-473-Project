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

    def add_user_to_db(self,user):
        # Add user to database
        sql = "INSERT INTO login (username,password,email) VALUES (%s, %s, %s)"
        values = (user.username,user.password,user.email)
        user_cursor = self.db_connection.cursor()
        try:
            user_cursor.execute(sql, values)
            self.db_connection.commit()
            user_cursor.close()
            return True
        except:
            user_cursor.close()
            return False

    def verify_credentials(self,user):
        #verify the user's credentials
        sql = "SELECT * FROM login WHERE email = %s AND password = %s"
        values = (user.email,user.password)
        user_cursor = self.db_connection.cursor()
        user_cursor.execute(sql,values)
        result = user_cursor.fetchall()
        if result:
            return True
        else:
            return False

    def change_password_in_db(self,user):
        #change the password in db
        return True

    def get_username(self,user):
        #with email address and password, get username
        pass
