# Part A

course_name = "Python"

def create_course_name():
    course_name = "Java"
    print(course_name)

create_course_name()
print(course_name)

# The first call prints the local variable and the second prints the global variable.

def local_counter(numbers):
    counter = 0
    for number in numbers:
        counter += number
    return counter

# We cannot access counter over here, we have to call the function first and store
# the returned value.

number = 10

def modify_global():
    global number
    number += 10

modify_global()

# We get UnboundLocalError: cannot access local variable 'number' where it is not associated with a value
# if we acces number without the global statement.

def outer():
    message = "Hello from outer"

    def inner():
        print(message)  # Enclosing-scope lookup: finds message from outer()

    inner()

outer()

# Part B

def add_all(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total

total = add_all(2321,4214,34,532,5532,432,4)
print(total)

def average(*numbers):
    if len(numbers) == 0:
        print("No numbers were provided")
        return 0
    else:
        total = 0
        for number in numbers:
            total += number
        average = total / len(numbers)
        return average

print(average())
print(average(231,3,4,1,43242,123,2))

def longest_word(*words):
    longest_length = 0
    for word in words:
        if len(word) >= longest_length:
            longest_length = len(word)
    return longest_length

longest = longest_word("abba", "kadabra", "lol")
print(longest)

def build_sentence(separator, *words):
    sentence = ""
    for word in words:
        sentence += f"{word}{separator}"
    return sentence

sentence = build_sentence(" ", "this", "is", "fun")
print(sentence)

def describe_scores(student_name, *scores):
    total = 0
    for score in scores:
        total += score
    average = total / len(scores)
    sentence = f"{student_name} Scores: "
    for score in scores:
        sentence += f"{score} "
    sentence += f"Average: {average}"
    return sentence

result = describe_scores("John", 43,43,234,1,43,24,1)
print(result)

# Part C

def positional(a, b, c):
    return a + b + c

numbers = [10, 20, 30]
result = positional(*numbers)
print(result)

tuple = ("Martin", "Pettersson", "Stockholm")

def tuple_function(first_name, last_name, city):
    print(first_name)
    print(last_name)
    print(city)

tuple_function(*tuple)

# Use starred assignment: first, *middle, last = values. Test with several list lengths.

# * in a function definition means that there are one or several arguments to be passed.
# * in a function call means that the argument will be unpacked.

# Part D

def show_profile(**info):
    for key, value in info.items():
        print(key, value)

show_profile(name = "harry", age = 12, profession = "wizard")

def build_product(name, price, **metadata):
    dict = metadata
    dict["name"] = name
    dict["price"] = price
    return dict

result = build_product(name="iPhone", price=140, color = "black", size = 128)
for key, value in result.items():
    print(key, value)

def create_settings(**settings):
    dict = {}
    for key, value in settings.items():
        if value is not None:
            dict[key] = value
    return dict

result = create_settings(color="black", mode=None, os = "Windows")

for key, value in result.items():
    print(key, value)

def normal_function(name, job, age):
    print(name)
    print(job)
    print(age)

dict = {"name" : "Martin", "age" : 35, "job" : "Programmer"}

normal_function(**dict)

# Part E

def log_event(event_type, *messages, **metadata):
    dict = {}
    dict["event_type"] = event_type
    i = 0
    for message in messages:
        i += 1
        dict[f"message_{i}"] = message
    for key, value in metadata.items():
        dict[key] = value
    return dict

result = log_event("party", "hello", "Stockholm", "Lexicon", date="September 15", weather="sunny")

for key, value in result.items():
    print(key, value)

def calculate_order(customer, *prices, **options):
    total = 0
    discount_percent = 0
    shipping_fee = 0
    if "discount" in options:
        discount_percent = options["discount"]
    if "fee" in options:
        shipping_fee = options["fee"]
    for price in prices:
        total += price
    total += shipping_fee
    discount = (100 - discount_percent) / 100
    total *= discount
    return (customer, total)

result = calculate_order("Martin", 42, 432, 234, 532, fee = 120, discount = 20)
print(result)

# Creates a 3D vector, more readable than with using **kwargs
def create_vector(x, y, z):
    return [x, y, z]

# Using **kwargs, less readable than the one above.
def create_vector_kwargs(**coordinates):
    vector = []
    for value in coordinates.values():
        vector.append(value)
    return vector

vector1 = create_vector_kwargs(a = 1, b = 2, c = 3, d = 4, e = 5)
vector2 = create_vector_kwargs(a = 1, b = 2, c = 3, d = 4, e = 5, f = 432, g = 52)
vector3 = create_vector_kwargs(a = 1, b = 2, c = 3, d = 4, e = 5, f = 432, g = 52, h = 123,  i = 432)

print(vector1, vector2, vector3)

# Part F

# Each section is a string, section keys are numbered
def create_report(title, *sections, **metadata):
    dict = {}
    dict["title"] = title
    i = 0
    for section in sections:
        i += 1
        dict[f"section_{i}"] = section
    for key, value in metadata.items():
        dict[key] = value
    return dict

report = create_report("Master Thesis", "Introduction", "Method", "Results", pages=120, author = "Martin", department = "Lexicon", version = 1.0, confidential = True, date = "September 15 2026")

print(report)

def summarize_report(report):
    for key, value in report.items():
        print(key, value)

summarize_report(report)

def count_words(*sections):
    count = 0
    for section in sections:
        words = section.split(" ")
        number_of_words = len(words)
        count += number_of_words
    return count

result = count_words("This is a sentence", "lol", "Roses are red violets are blue")
print(result)

# Part G

default_dict = {"name" : "martin", "age" : 35, "strong" : True}

def merge_settings(defaults, **overrides):
    return_dict = defaults
    for key, value in overrides.items():
        return_dict[key] = value
    return return_dict

print(merge_settings(default_dict, color="silver", bank="nordea"))

def call_summary(function_name, *args, **kwargs):
    return_string = f"{function_name}("
    for arg in args:
        return_string += f"{arg},"
    for key, value in kwargs.items():
        return_string += f"{key}={value},"
    return_string = return_string[:-1]
    return_string += f")"
    return return_string

print(call_summary("martin_func", 12, 32, name="martin", age=12))


