class db():

    def __init__(self):
        import mysql.connector as mysql
        from backend.db_connection import db_connection
        parent_db = db_connection()
        self.db_connection = mysql.connect(host=parent_db.HOST, database=parent_db.DATABASE, user=parent_db.USER, password=parent_db.PASSWORD)

    def add_schedule_to_db(self,schedule):
        sql = "INSERT INTO schedule (schedule_id, email, passcode, added_by) VALUES (%s, %s, %s, %s)"
        values = (schedule.schedule_id, schedule.email, schedule.passcode, schedule.email)
        user_cursor = self.db_connection.cursor()
        user_cursor.execute(sql, values)
        self.db_connection.commit()
        user_cursor.close()
        return True
