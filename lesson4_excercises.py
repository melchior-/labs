# Part A

def greet():
    print("Hello")

def show_course_name():
    print("Java")

def print_separator():
    print("")

greet()
greet()
print_separator()
show_course_name()
show_course_name()
print_separator()

def greet(name):
    print(f"Hello {name}")

def introduce(name, city):
    print(f"Hello {name}, you are from {city}")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b): # This is a parameter
    return a / b

divide(10, 2) # This is an argument

def calculate_area(width, height):
    return width * height

depth = 10
volume = calculate_area(4, 8) * depth

# Part B

def is_even(number):
    return number % 2 == 0

def get_larger(a, b):
    if a >= b:
        return a
    else:
        return b
    
def classify_score(score):
    if score >= 60:
        return "PASS"
    else:
        return "FAIL"

def full_name(first_name, last_name):
    return f"{first_name} {last_name}"

def calculate_discount(price, percent):
    discount = (100 - percent) / 100
    return price * discount

def print_result():
    result = "lol"
    print(result) # Here, result will be printed in the terminal

def get_result():
    result = "lol"
    return result # Here nothing will print, instead the string will be returned to the caller.

# Part C

def greet(name, greeting):
    print(f"{greeting} {name}")

name = "Martin"

greet(name, greeting="Hello")

def calculate_price(price, quantity, discount):
    discount = (100 - discount) / 100
    total_price = price * quantity * discount
    return total_price

price = 150

calculate_price(price, quantity=1, discount=0)

def create_profile(name, city, active):
    dict = {"name" : name, "city" : city, "active" : active}
    return dict

name = "Martin"
create_profile(name, city='Unknown', active=True)

calculate_price(price, discount=20, quantity=4)

# INVALID default-parameter ordering:
# def example(a=1, b):
#     return a + b
#
# This is invalid because Python requires all non-default parameters
# (like b) to come before any default parameters (like a=1).
# Otherwise, Python cannot reliably know which arguments are required
# and which ones have default values.

# Part D

def calculate_total(numbers):
    sum = 0
    for number in numbers:
        sum += numbers
    return sum

