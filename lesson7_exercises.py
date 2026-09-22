# Part A

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

# Part B

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

# Part C

class Product():
    tax_rate = 25

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def price_with_tax(self):
        tax_modifier = self.tax_rate / 100 + 1
        price_tax = tax_modifier * self.price
        return price_tax

    def update_tax_rate(self, rate):
        self.tax_rate = rate

product1 = Product("Hammer", 100)
print(product1.price_with_tax())
product2 = Product("Mose", 200)
print(product2.price_with_tax())
product3 = Product("Keyboard", 400)
print(product3.price_with_tax())

Product.tax_rate = 35
print(product1.price_with_tax())
print(product2.price_with_tax())
print(product3.price_with_tax())

product1.update_tax_rate(45)
print(product1.tax_rate)
print(product2.tax_rate)
print(Product.tax_rate)

# Part D

class Student():
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_status(self):
        if self.score >= 70:
            return "PASS"
        return "FAIL"

student1 = Student("Anna", 70)
student2 = Student("Charles", 80)
student3 = Student("Martin", 55)
student4 = Student("Bob", 45)
student5 = Student("George", 32)
student6 = Student("John", 100)

list_of_students = [student1, student2, student3, student4, student5, student6]

for student in list_of_students:
    print(f"{student.name} {student.score}")

for student in list_of_students:
    print(f"{student.name} {student.get_status()}")

passing_students = [student.name for student in list_of_students if student.score >= 70]
print(passing_students)

# Part E

class Teacher():
    def __init__(self, name):
        self.name = name

class Course():
    students = []
    
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher

    def add_student(self, student):
        self.students.append(student)

teacher1 = Teacher("Bob")
course1 = Course("Java", teacher1)

print(f"{course1.name} {course1.teacher.name}")

course1.add_student(student1)
course1.add_student(student2)
course1.add_student(student3)

for student in course1.students:
    print(f"{student.name}")


