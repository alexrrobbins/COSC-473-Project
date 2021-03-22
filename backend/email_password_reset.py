from backend.email import Email

class EmailPwdReset(Email):

    def send_pwd_reset_message(self):
        sent_from = 'schedulesheep@gmail.com'
        to = self.recipient_address
        subject = 'Password Reset'
        body = "Hello, you have requested a password reset on schedulesheep.com, for user with email address: " + self.recipient_address

        email_text = """\
        From: %s
        To: %s
        Subject: %s

        %s
        """ % (sent_from, ", ".join(to), subject, body)
        return self.send_message(email_text)
