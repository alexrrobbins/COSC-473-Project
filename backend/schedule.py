from backend.db_schedule import db
import math, random

class Schedule():

    def __init__(self,schedule_id,email,passcode,added_by):
        self.schedule_id = schedule_id
        self.email = email
        self.passcode = passcode
        self.added_by = added_by
        self.our_db = db()

    # Getters - return strings
    def get_id(self):
        return self.schedule_id

    def get_owner(self):
        return self.email

    def get_passcode(self):
        self.passcode = str(math.floor(random.random() * 100000))
        return self.passcode

    # These functions return true or false based on whether the db actions were successful

    def add_to_db(self):
        return self.our_db.add_schedule_to_db(self)
