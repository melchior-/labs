# Part A

class BadTeam():

    def __init__(self, name, members = []):
        self.name = name
        self.members = members

    def add_member(self, new_member):
        self.members.append(new_member)

team1 = BadTeam("Hawks")
team2 = BadTeam("Lions")

team1.add_member("Martin")

print(team1.members)
print(team2.members)

# The member gets added to both teams. memers=[] is a default argument, and Python creates that list once when the function is defined, not once per instance.

class Team():
    def __init__(self, name, members = None):
        self.name = name
        self.members = [] if members is None else members

    def add_member(self, new_member):
        self.members.append(new_member)

team1 = Team("Hawks")
team2 = Team("Lions")

team1.add_member("Martin")

print(team1.members)
print(team2.members)

# Part B

movie_dict = {"title" : "Forrest Gump", "director" : "Robert Zemeckis", "rating" : 8.0}

class Movie():
    def __init__(self, title, director, rating):
        self.title = title
        self.director = director
        self.rating = rating

    def is_highly_rated(self):
        if self.rating >= 7.9:
            return True
        return False

# I would choose the dictionary if there is no behavior needed for the movies or repeated objects. If we need validation or logic to be used on the movies I would choose a class.

# Part C

class Account():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

class SavingsAccount(Account):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

account1 = Account("Martin", 1000)
savings1 = SavingsAccount("Bob", 2000, 10)

print(account1.balance)
print(account1.owner)
print(savings1.balance)
print(savings1.owner)
print(savings1.interest_rate)

# A SavingsAccount is a type of Account.

# Part D

class Employee():
    def __init__(self, name):
        self.name = name

    def get_information(self):
        return self.name

class Developer(Employee):
    def __init__(self, name):
        super().__init__(name)

    def programming_language(self):
        return "Python"

class Manager(Employee):
    def __init__(self, name):
        super().__init__(name)

    def manage(self):
        return "Woof!"

e = Employee("Martin")
# Cannot run e.programming_language() since e is not a developer subclass instance.

# Part E

class Device():
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def initialize(self):
        if self.year < 0:
            raise ValueError("Year cannot be negative.")
        is_active = True

class Laptop(Device):
    def __init__(self, brand, year, ram_gb):
        super().__init__(brand, year)
        self.ram_gb = ram_gb

class Phone(Device):
    def __init__(self, brand, year, color):
        super().__init__(brand, year)
        self.color = color

laptop = Laptop("Dell", 2022, 16)
phone = Phone("Apple", 2025, "white")

laptop.initialize()
phone.initialize()

# Part F

class Notification():
    def __init__(self):
        pass

    def send(self):
        return "Sent from base class!"

class EmailNotification(Notification):
    def __init__(self):
        super().__init__()

    def send(self):
        return "Email!"

class SMSNotification(Notification):
    def __init__(self):
        super().__init__()

    def send(self):
        return "SMS!"

notif = Notification()
email = EmailNotification()
sms = SMSNotification()

print(notif.send()) # Send is used from base class
print(email.send()) # Send is used from email class
print(sms.send()) # Send is used from the SMS class

# Part G

class Report():
    def __init__(self, author, pages):
        self.author = author
        self.pages = pages

    def get_summary(self):
        print(f"Author: {self.author}, Pages: {self.pages}")

class SalesReport(Report):
    def __init__(self, author, pages, revenue):
        super().__init__(author, pages)
        self.revenue = revenue

    def get_summary(self):
        super().get_summary()
        print(f"Revenue: {self.revenue}")

sr = SalesReport("Martin", 100, 10000)
sr.get_summary()

# Part H

class User():
    def __init__(self, username, email):
        if "@" not in email:
            raise ValueError("Email must contain @.")

        self.username = username
        self.email = email

    def present_user(self):
        print(f"Name: {self.username}, Email: {self.email}")

    def greet(self):
        print(f"Hello, I am {self.username} with email {self.email}.")

class AdminUser(User):
    def __init__(self, username, email, privilege):
        super().__init__(username, email) 
        self.privilege = privilege

    def get_privilege(self):
        return self.privilege

    def greet(self):
        super().greet()
        print(f"I am an Admin.")

class PremiumUser(User):
    def __init__(self, username, email, subscription_type):
        super().__init__(username, email)
        self.subscription_type = subscription_type

    def get_subscription(self):
        return self.subscription_type

    def greet(self):
        super().greet()
        print(f"I am a Premium User.")

first_user = User("Martin", "martin.pettersson@outlook.com")
second_user = AdminUser("Hilda", "hilda123@gmail.com", "IT-Admin")
third_user = PremiumUser("Greg", "greg@yahoo.com", "Six-month")

first_user.present_user()
second_user.greet()
third_user.greet()
first_user.greet()
third_user.present_user()
second_user.get_privilege()
third_user.get_subscription()

# AdminUser is a type of User
# PremiumUser is (also) a type of User