class EmailNotification:
    def send(self):
        return "Sent from Email"

class SMSNotification:
    def send(self):
        return "Sent from SMS"

class PushNotification:
    def send(self):
        return "Sent from push"

email = EmailNotification()
sms = SMSNotification()
push = PushNotification()

list_of_items = [email, sms, push]

for item in list_of_items:
    print(item.send())

