class db():

    def __init__(self):
        import mysql.connector as mysql
        from backend.db_connection import db_connection
        parent_db = db_connection()
        self.db_connection = mysql.connect(host=parent_db.HOST, database=parent_db.DATABASE, user=parent_db.USER, password=parent_db.PASSWORD)

##############Schedule methods####################
    def add_schedule_to_db(self,schedule):
        sql = "INSERT INTO schedule (schedule_id, email, passcode, added_by) VALUES (%s, %s, %s, %s)"
        values = (schedule.schedule_id, schedule.email, schedule.passcode, schedule.email)
        return self.schedule_helper(sql,values)

    def delete_schedule_from_db(self,schedule):
        sql = "DELETE FROM schedule WHERE schedule_id = %s AND email = %s"
        values = (schedule.schedule_id,schedule.email)
        return self.schedule_helper(sql,values)

    def retrieve_schedule_from_db(self, schedule):
        sql = "SELECT email FROM schedule WHERE schedule_id = %s AND passcode = %s"
        values = (schedule.schedule_id, schedule.passcode)
        schedule_cursor = self.db_connection.cursor()
        schedule_cursor.execute(sql,values)
        email = schedule_cursor.fetchall()[0][0]
        if email:
            schedule.set_email(email)
            return True
        else:
            return False

    def schedule_helper(self,sql,values):
        schedule_cursor = self.db_connection.cursor()
        schedule_cursor.execute(sql,values)
        try:
            self.db_connection.commit()
            return True
        except:
            return False

##############Event methods##############
    def add_event_to_db(self, event):
        sql = "INSERT INTO event (schedule_id, title, date, time) VALES (%s, %s, %s, %s)"
        values = (event.schedule_id, event.title, event.date, event.time)
        return self.schedule_helper(sql,values)
