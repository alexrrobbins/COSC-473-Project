import smtplib
from email.message import EmailMessage

class Email():

    def __init__(self,recipient_address):
        self.recipient_address = recipient_address
        self.session = smtplib.SMTP('smtp.gmail.com', 587)
        self.session.starttls()
        # Dummy Google account created for the project
        self.session.login("schedulesheep@gmail.com", "IUPcosc1!")

    def send_message(self,message):
        self.session.sendmail("schedulesheep@gmail.com", self.recipient_address, message)
        self.session.quit()
        return True
