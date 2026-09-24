# Part A

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

# Python uses duck typing: if an object has the method you call, it works

# Part B

class Document:
    def __init__(self, title):
        self.title = title

    def describe(self):
        return "Normal document"

class PDFDocument(Document):
    def __init__(self, title):
        super().__init__(title)

    def describe(self):
        return "PDF"

class TextDocument(Document):
    def __init__(self, title):
        super().__init__(title)

    def describe(self):
        return "Text Document"

pdf1 = PDFDocument("Bill")
pdf2 = PDFDocument("CV")
text1 = TextDocument("Receipt")
text2 = TextDocument("Newspaper")

list_of_documents = [pdf1, pdf2, text1, text2]

for document in list_of_documents:
    print(f"{document.title} {document.describe()}")

# Part C

class Printer:
    def display_status(self):
        return "Printer"

class Screen:
    def display_status(self):
        return "Screen"

printer = Printer()
screen = Screen()

products = [printer, screen]

for product in products:
    print(product.display_status())

# It works because both classes implement the same interface

# Part D
