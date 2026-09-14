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

