from backend.email import Email
import random, string

class EmailPwdReset(Email):

    def send_pwd_reset_message(self):
        seed = string.ascii_letters
        temp_pin = ''.join(random.choice(seed) for i in range(10))
        email_text = "From: {}\nTo: {}\nSubject: {}\n\n\{}\n{}".format("schedulesheep@gmail.com", self.recipient_address,"Password Reset",
            "Hello, you have requested a password reset on schedulesheep.com. Your password reset pin is ",temp_pin)

        return self.send_message(email_text)
