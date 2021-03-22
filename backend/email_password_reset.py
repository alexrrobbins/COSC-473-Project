from backend.email import Email

class EmailPwdReset(Email):

    def send_pwd_reset_message(self):
        return self.send_message("<!DOCTYPE html><p>Hello, you have requested a password reset on schedulesheep.com, for user with email address: " + self.email + "</p></html>")
