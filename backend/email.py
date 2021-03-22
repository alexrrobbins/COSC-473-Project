import smtplib
from email.message import EmailMessage

class Email():

    def __init__(self,recipient_address):
        self.recipient_address = recipient_address
        self.server = smtplib.SMTP('smtp.gmail.com', 587)
        self.server.ehlo()
        self.server.starttls()
        # Dummy Google account created for the project
        self.server.login("schedulesheep@gmail.com", "IUPcosc1!")

    def send_message(self,message):
        self.server.sendmail("schedulesheep@gmail.com", self.recipient_address, message)
        self.server.close()
        return True
