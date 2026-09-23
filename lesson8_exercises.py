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
        super.__init__(name)

    def programming_language(self):
        return "Python"

class Manager(Employee):
    def __init__(self, name):
        super.__init__(name)

    def manage(self):
        return "Woof!"

e = Employee("Martin")
# Cannot run e.programming_language() since e is not a developer subclass instance.

