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

def count_even(numbers):
    count = 0
    for number in numbers:
        if number % 2 == 0:
            count += 1
    return count

def get_long_words(words, minimum_length):
    long_words = []
    for word in words:
        if len(word) >= minimum_length:
            long_words.append(word)
    return long_words

def find_student(students, name):
    for student in students:
        if student["name"] == name:
            return student
    return None

def average_score(students):
    number_of_students = len(students)
    total_score = 0
    for student in students:
        total_score += student["score"]
    return total_score / number_of_students

def get_active_users(users):
    active_users = []
    for user in users:
        if user["active"]:
            active_users.append(user)
    return active_users
        
# Part E

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def classification(celsius):
    if celsius >= 24:
        return "hot"
    elif celsius >= 15:
        return "warm"
    else:
        return "cold"

def format_fahrenheit(fahrenheit):
    return f"{fahrenheit:.2f}"

def temperature_report(celsius):
    print(f"It is {celsius} degrees outside.")
    temp_type = classification(celsius)
    print(f"It is {temp_type}.")
    fahrenheit = celsius_to_fahrenheit(celsius)
    fahrenheit = format_fahrenheit(fahrenheit)
    print(f"Fahrenheit value: {fahrenheit}")

def order_calculation(subtotal, discount, final_total):
    return (subtotal + final_total) * discount

# Refactor average_score
def number_of_students(students):
    return len(students)

def total_score(students):
    total_score = 0
    for student in students:
        total_score += student["score"]
    return total_score

def average_student_score(total_score, number_of_students):
    return total_score / number_of_students

# Part F

def normalize_name(name):
    name = name.strip()
    name = name.capitalize()
    return name

def validate_age(age):
    if age >= 18:
        return True
    return False

def registration_fee(age, status):
    if age < 18 and status == "student":
        return 100
    else:
        return 150

participant_dict = [
    {"name" : "bob jones", "status" : "student", "age" : 32, "valid_age" : True, "fee" : 100},
    {"name" : "alice jones", "status" : "student", "age" : 12, "valid_age" : True, "fee" : 100},
    {"name" : "tom jones", "status" : "student", "age" : 14, "valid_age" : True, "fee" : 100},
    {"name" : "ken richard", "status" : "student", "age" : 55, "valid_age" : True, "fee" : 100},
    {"name" : "bob jones", "status" : "student", "age" : 32, "valid_age" : True, "fee" : 100},
    {"name" : "martin pettersson", "status" : "student", "age" : 12, "valid_age" : True, "fee" : 100},
    {"name" : "bob clark", "status" : "student", "age" : 14, "valid_age" : True, "fee" : 100},
    {"name" : "john smith", "status" : "student", "age" : 55, "valid_age" : True, "fee" : 100}
]

def update_participants(participants):
    for participant in participants:
        participant["name"] = normalize_name(participant["name"])
        participant["valid_age"] = validate_age(participant["age"])
        participant["fee"] = registration_fee(participant["age"], participant["status"])
    return participants

def registration_revenue(participants):
    total = 0
    for participant in participants:
        total += participant["fee"]
    return total

def only_students(participants):
    students = []
    for participant in participants:
        if participant["status"] == "student":
            students.append(participant)
    return students

def oldest_participant(participants):
    oldest = 0
    for participant in participants:
        if participant["age"] > oldest:
            oldest = participant["age"]
    return oldest

def summary_string(participant):
    status = "No"
    if participant["status"]:
        status = "Yes"
    str = f"Name: {participant["name"]}, Status: {participant["status"]}, Age: {participant["age"]}, Valid age: {status}, Registration fee: {participant["fee"]}"
    return str

# Part G

def min_and_max(numbers):
    min_ = numbers[0]
    max_ = numbers[0]

    for number in numbers:
        if number >= max_:
            max_ = number
        elif number <= min_:
            min_ = number

    return max_, min_

def is_palindrome(word):
    palindrome = word[::-1]
    print(palindrome)
    if palindrome == word:
        return True
    else:
        return False

def character_frequency(word):
    dict = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0}
    for char in word:
        dict[char] = dict[char] + 1
    return dict

def count_characters(text):
    frequencies = {}

    for char in text:
        if char in frequencies:
            frequencies[char] += 1
        else:
            frequencies[char] = 1

    return frequencies

def posnegzero(numbers):
    dict = {"pos":0, "neg":0, "zero":0}

    for number in numbers:
        if number > 0:
            dict["pos"] += 1
        elif number < 0:
            dict["neg"] += 1
        else:
            dict["zero"] += 1

    return dict

# Main program

if __name__ == "__main__":
    name = "Martin"
    create_profile(name, city='Unknown', active=True)

    calculate_price(price, discount=20, quantity=4)

    dict = character_frequency("lfksdfdfs")

    a, b = min_and_max([321,42,32532,5324,123,231])
    print(f"{a},{b}")
    print(dict)

    participants = update_participants(participant_dict)
    print(registration_revenue(participants))
    print(only_students(participants))
    print(oldest_participant(participants))
    print(summary_string(participants[0]))

    print(is_palindrome("anna"))

    print(count_characters("addkaslmlkdm"))

    total = 100

    def add_tax():
        return total * 1.25

    print(add_tax())