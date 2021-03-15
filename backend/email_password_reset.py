from backend.email import Email

class EmailPwdReset(Email):

    def send_pwd_reset_message(self):
        return self.send_message("Hello, you have requested a password reset on schedulesheep.com, please follow the link below to reset your password:")
