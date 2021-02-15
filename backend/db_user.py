class db():

    def __init__(self):
        import mysql.connector as mysql
        from backend.db_connection import db_connection
        parent_db = db_connection()
        self.db_connection = mysql.connect(host=parent_db.HOST, database=parent_db.DATABASE, user=parent_db.USER, password=parent_db.PASSWORD)

###########Register and login functions##################

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
        result = self.get_user_from_db(user)
        if result:
            return True
        else:
            return False

    def get_username(self,user):
        result = self.get_user_from_db(user)
        return result[0][0]

    def check_admin_status(self,user):
        result = self.get_user_from_db(user)
        if result[0][3] == 1:
            return True
        else:
            return False

    def get_user_from_db(self,user):
        sql = "SELECT * FROM login WHERE email = %s AND password = %s"
        values = (user.email,user.password)
        user_cursor = self.db_connection.cursor()
        user_cursor.execute(sql,values)
        result = user_cursor.fetchall()
        user_cursor.close()
        return result

###############NOT TESTED##################
    def change_password_in_db(self,user,new_password):
        sql = "UPDATE `login` SET `password` = %s WHERE `login`.`email` = %s"
        values = (user.email,new_password)
        return admin_helper(sql,values)

    def remove_user_from_db(self,user):
        sql = "DELETE FROM 'login' WHERE 'login'.'email' = %s"
        values = (user.email)
        return admin_helper(sql,values)

    def promote_to_admin(self,user):
        sql = "UPDATE `login` SET `admin` = '1' WHERE `login`.`email` = %s"
        values = (user.email)
        return admin_helper(sql,values)

    def admin_helper(self,sql,values):
        user_cursor = self.db_connection.cursor()
        user_cursor.execute(sql,values)
        try:
            self.db_connection.commit()
            return True
        except:
            return False
