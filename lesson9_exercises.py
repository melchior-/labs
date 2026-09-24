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

class User:
    def __init__(self, name):
        self.name = name

    def isinstance(self):
        return type(self)

class AdminUser(User):
    def __init__(self, name):
        super().__init__(name)

    def isinstance(self):
        return type(self)

user = User("Martin")
admin = AdminUser("Hilda")
word = "String"

print(user.isinstance())
print(admin.isinstance())
print(type(word))

# AdminUser is also an instance of User because of inheritance

# Part E

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"This is a {self.name} with price {self.price}"

product = Product("Laptop", 10000)
print(product)
product2 = Product("Phone", 5000)
product3 = Product("Keyboad", 300)

print(product2)
print(product3)

str_product = str(product2)
print(type(str_product))

# Part F

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"This is an account with owner {self.owner} and balance {self.balance}."

class SavingsAccount(Account):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def __str__(self):
        return super().__str__() + f" Interest rate: {self.interest_rate}."

account = Account("Martin", 1000)
savings = SavingsAccount("Hilda", 2000, 19)

print(account)
print(savings)