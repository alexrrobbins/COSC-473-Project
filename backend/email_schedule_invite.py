from backend.email import Email

class EmailInvite(Email):
    def send_schedule_invite(self,username,schedule_id,passcode):
        email_text = "From: {}\nTo: {}\nSubject: {}\n\nHello,\n{} has invited you to view their schedule.\nThe schedule id is {} and the passcode is {}.".format(
        "schedulesheep@gmail.com", self.recipient_address,"Schedule Invite",schedule_id,passcode)
        return self.send_message(email_text)
