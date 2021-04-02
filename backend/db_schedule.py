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

    def retrieve_all_schedules(self,email):
        sql = "SELECT * FROM schedule WHERE email = %s"
        values = (email,)
        user_cursor = self.db_connection.cursor()
        user_cursor.execute(sql,values)
        return user_cursor.fetchall()

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
        sql = "INSERT INTO event (Title, Date, schedule_id) VALUES (%s, %s, %s)"
        values = (event.title, event.date, event.schedule_id)
        return self.schedule_helper(sql,values)

    def retrieve_all_events(self,id):
        sql = "SELECT * FROM event WHERE schedule_id = %s"
        values = (id,)
        event_cursor = self.db_connection.cursor()
        event_cursor.execute(sql,values)
        return event_cursor.fetchall()

    def delete_event_from_db(self):
        sql = "DELETE FROM event WHERE Title = %s AND Date = %s AND schedule_id = %s"
        values = (event.title, event.date, event.schedule_id)
        return self.schedule_helper(sql,values)

##############Search methods###############
# Need to be tested, the sql might be wrong
    def search_by_title(self,schedule_id,title):
        sql = "SELECT (Title, Date) FROM event WHERE schedule_id = %s AND Title LIKE %%s%"
        values = (schedule_id, title)
        event_cursor = self.db_connection.cursor()
        event_cursor.execute(sql,values)
        return event_cursor.fetchall()

    def search_by_date(self,schedule_id,date):
        sql = "SELECT (Title, Date) FROM event WHERE schedule_id = %s AND Date LIKE %%s%"
        values = (schedule_id, date)
        event_cursor = self.db_connection.cursor()
        event_cursor.execute(sql,values)
        return event_cursor.fetchall()
