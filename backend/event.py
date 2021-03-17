from backend.db_schedule import db

class Event():

    def __init__(self, schedule_id, date, title):
        self.schedule_id = schedule_id
        self.date = date
        self.title = title
        self.time = time
        self.our_db = db()

    def get_title(self):
        return self.title

    def get_date(self):
        return self.date

    def add_to_db(self):
        return self.our_db.add_event_to_db(self)
