class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author 
        self.pages = pages

    def is_long(self):
        if (self.pages > 300):
            return True
        return False

book1 = Book("A Dance with Dragons", "George RR Martin", 1100)
book2 = Book("Frankenstein", "Mary Shelley", 400)
book3 = Book("Red Rising", "Pierce Brown", 350)
book4 = Book("Angels and Demons", "Dan Brown", 500)

print(book1.title)
print(book1.author)
print(book1.pages)

class Laptop():
    def __init__(self, brand, model, ram_gb=8, price=7000):
        self.brand = brand
        self.model = model
        self.ram_gb = ram_gb
        self.price = price

laptop1 = Laptop("Dell", "XPS", 16, 8000)
laptop2 = Laptop("HP", "Pavilion", 32, 10000)
laptop3 = Laptop("Apple", "MacBook", 128, 21000)

laptop3.price = 18000

l = Laptop("Dell", "XPS", 16, 8000)
r = Laptop("Dell", "XPS", 16, 8000)

print(l is r)

laptop4 = Laptop("HP", "SuperLaptop", ram_gb = 64, price = 9000)

print(laptop4.brand)
print(laptop4.model)
print(laptop4.ram_gb)
print(laptop4.price)

class BankAccount():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if (self.balance - amount < 0):
            raise ValueError("Balance cannot be negative")
        self.balance -= amount

class Task():
    def __init__(self, title, completed=False):
        self.title = title
        self.completed = completed

    def complete(self):
        self.completed = True

    def reopen(self):
        self.completed = False

ba = BankAccount("Martin", 500)
ba2 = BankAccount("George", 400)
ba.withdraw(500)
print(ba.balance)
print(ba2.balance)


