# db - class provides the link between the MySQL db and the User and Admin classes

class db():

    # Initialize new database connection
    # DB credentials are stored in db_connection class
    def __init__(self):
        import mysql.connector as mysql
        from backend.db_connection import db_connection
        parent_db = db_connection()
        self.db_connection = mysql.connect(host=parent_db.HOST, database=parent_db.DATABASE, user=parent_db.USER, password=parent_db.PASSWORD)

###########Register and login functions##################

    # Add user to database through registration or admin add user
    # If user added successfully, return true, otherwise false
    def add_user_to_db(self,user):
        sql = "INSERT INTO login (username,password,email,AddedBy) VALUES (%s, %s, %s, %s)"
        values = (user.username,user.password,user.email,user.email)
        user_cursor = self.db_connection.cursor()
        try:
            user_cursor.execute(sql, values)
            self.db_connection.commit()
            user_cursor.close()
            return True
        except:
            user_cursor.close()
            return False

    #Verify the user's credentials, true if successful login, false otherwise
    def verify_credentials(self,user):
        result = self.get_user_from_db(user)
        if result:
            return True
        else:
            return False

    # Retrieve the username from the db query, returns a string
    def get_username(self,user):
        result = self.get_user_from_db(user)
        return result[0][0]

    # Retrieve the admin flag from a user, true if admin false otherwise
    def check_admin_status(self,user):
        result = self.get_user_from_db(user)
        if result[0][3] == 1:
            return True
        else:
            return False

    # Helper function to retrieve any user from the database using an email and password
    # returns true if user found, false otherwise
    def get_user_from_db(self,user):
        sql = "SELECT * FROM login WHERE email = %s AND password = %s"
        values = (user.email,user.password)
        user_cursor = self.db_connection.cursor()
        user_cursor.execute(sql,values)
        result = user_cursor.fetchall()
        user_cursor.close()
        return result

###############Admin functionality##################

    # Helper method to return true if admin's action is successful, false otherwise
    def admin_helper(self,sql,values):
        user_cursor = self.db_connection.cursor()
        user_cursor.execute(sql,values)
        try:
            self.db_connection.commit()
            return True
        except:
            return False

    # Change a user's password given an email
    def change_password_in_db(self,email,new_password):
        sql = "UPDATE login SET password = %s WHERE email = %s"
        values = (new_password,email)
        return self.admin_helper(sql,values)

    # Delete a user from db given an email
    def remove_user_from_db(self,email):
        sql = "DELETE FROM login WHERE email = %s"
        values = (email,)
        return self.admin_helper(sql,values)

    # Promote a user to admin given an email
    def promote_to_admin(self,email):
        sql = "UPDATE login SET admin = 1 WHERE email = %s"
        values = (email,)
        return self.admin_helper(sql,values)

    # Admin add user - basically change the addedby column in db
    def admin_add_user_to_db(self,user,adminEmail):
        if self.add_user_to_db(user):
            sql = "UPDATE login SET AddedBy = %s WHERE email = %s"
            values = (adminEmail,user.get_email())
            self.admin_helper(sql,values)
            return True
        else:
            return False

##############Admin view functionality#####################
    def list_users(self):
        sql = "SELECT * FROM LOGIN"
        user_cursor = self.db_connection.cursor()
        user_cursor.execute(sql)
        return user_cursor.fetchall()
