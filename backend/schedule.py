from backend.db_schedule import db
import math, random, string

class Schedule():

    def __init__(self,email,schedule_id='null',passcode='null,',added_by='null'):
        self.schedule_id = schedule_id
        self.email = email
        self.passcode = passcode
        self.added_by = added_by
        self.our_db = db()

    # Getters - return strings
    def get_id(self):
        seed = string.ascii_letters
        self.schedule_id = ''.join(random.choice(seed) for i in range(10))
        return self.schedule_id

    def get_static_id(self):
        return self.schedule_id

    def get_owner(self):
        return self.email

    def get_passcode(self):
        self.passcode = str(math.floor(random.random() * 100000))
        return self.passcode

    def set_email(self, email):
        self.email = email

    # These functions return true or false based on whether the db actions were successful

    def add_to_db(self):
        return self.our_db.add_schedule_to_db(self)

    def delete_from_db(self):
        return self.our_db.delete_schedule_from_db(self)

    def retrieve_schedule(self):
        return self.our_db.retrieve_schedule_from_db(self)

    def retrieve_all_schedules(self):
        return self.our_db.retrieve_all_schedules(self.email)

    def retrieve_all_events(self):
        return self.our_db.retrieve_all_events(self.schedule_id)

    # Search functions - returns matching events under schedule

    def search_by_title(self,title):
        return self.our_db.search_by_title(self.schedule_id,title)

    def search_by_date(self,date):
        return self.our_db.search_by_date(self.schedule_id,date)
