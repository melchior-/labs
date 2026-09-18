# Part A

def squares(numbers):
    squares = []
    for number in numbers:
        number = number ** 2
        squares.append(number)
    return squares

print(squares([23,32,4,2,1,6]))

def squares_comprehension():
    squares = [n ** 2 for n in range(1, 21)]
    return squares

print(squares_comprehension())

def even_numbers():
    even = [n for n in range(1, 101) if n % 2 == 0]

print(even_numbers())

def convert_names(names):
    converted = [name.strip().title() for name in names]
    return converted

print(convert_names(["martin", "hilda"]))

def passing_scores(scores):
    pass_threshold = 60
    passed = [s for s in scores if s >= pass_threshold]
    return passed

scores = [43, 53, 65, 90, 123, 12]
print(passing_scores(scores))

def label_scores(scores):
    labels = ["PASS" if score >= 60 else "FAIL" for score in scores]
    return labels

print(label_scores(scores))

def calculate_total_comp(numbers):
    total = sum(n for n in numbers)
    return total

def get_long_words_comp(words, minimum_length):
    long_words = [word for word in words if len(word) >= minimum_length]
    return long_words

def count_even_comp(numbers):
    evens = [n for n in numbers if n % 2 == 0]
    return len(evens)

print(calculate_total_comp([1, 2, 3, 4, 5]))
print(get_long_words_comp(["hej", "asdf", "martin"], 4))
print(count_even_comp([2, 4, 6, 8, 13, 124, 432, 43]))

# Part B

def squares_dict():
    squares_dict = {n: n ** 2 for n in range(1,11)}
    return squares_dict

print(squares_dict())

def words_length(words):
    lengths = {w: len(w) for w in words}
    return lengths

print(words_length(["martin", "sara", "anna"]))

def normalized_set(words):
    normalized = {word.strip().lower() for word in words}
    return normalized

print(normalized_set(["  MARTIN", "martin", "Martin   ", "Sara", "SARA", "Anna"]))

products = [
    {"name" : "Laptop", "price": 12000},
    {"name" : "iPhone", "price": 18000},
    {"name" : "Keyboard", "price": 2000},
    {"name" : "Mouse", "price": 1500}
]
threshold = 2000

threshold_dict = {product["name"]: product["price"] for product in products if product["price"] <= threshold}

print(threshold_dict)

students = [
    {"name" : "Martin", "score" : 100},
    {"name" : "Anna", "score" : 20},
    {"name" : "Sara", "score" : 30},
    {"name" : "Hilda", "score" : 80},
    {"name" : "Peter", "score" : 70}
]

student_dict = {student["name"]: "PASS" if student["score"] >= 70 else "FAIL" for student in students}

print(student_dict)

# Part C

tracks = ["Opalite", "Cheri Cheri Lady", "Merry Christmas", "Happy Birthday"]

for i, track in enumerate(tracks, start=1):
    print(f"{i}. {track}")

tasks = ["Clean the house", "Go shopping", "Go to work", "Play games"]

for i, task in enumerate(tasks, start=1):
    print(f"{i}. {task}")

def print_above_threshold(numbers, threshold):
    for i, number in enumerate(numbers):
        if (number >= threshold):
            print(f"{i} : {number}")

numbers = [32,243,52,4,52,66,345,73,54,13,2]
threshold = 70
print_above_threshold(numbers, 70)

numbers = [1, 2, 3, 4, 5, 6, 7]

# Original loop

for i in range(len(numbers)):
    print(f"{i}. {numbers[i]}")

# Enumerate, this one is more readable

for i, number in enumerate(numbers):
    print(f"{i}. {number}")

# Part D

names = ["Martin", "Bob", "Hilda", "Peter"]
scores = [100, 32, 42, 52]

combined = list(zip(names, scores))

print(combined)

keys = [1, 2, 3, 4, 5, 6]
values = ["Laptop", "iPhone", "Mouse", "Keyboard", "Mp3 Player", "Headphones"]

products = dict(zip(keys, values))

print(products)

#Here, we zip until we reach the end of the shorter list

length1 = [1,2,3,4,5]
length2 = [1,2,3,4,5,6,7]
combined = list(zip(length1, length2))
print(combined)

for a, b in zip(length1, length2):
    print(a, b)

a = 5
b = 3
a, b = b, a
print(a, b)

# Part E

words = ["martin", "hej", "lol", "Python", "America"]
sorted_words = sorted(words, key = len)
print(sorted_words)

students = [
    {"name" : "Martin", "score" : 100},
    {"name" : "Anna", "score" : 20},
    {"name" : "Sara", "score" : 30},
    {"name" : "Hilda", "score" : 80},
    {"name" : "Peter", "score" : 70}
]

students_ascending = sorted(students, key = lambda student: student["score"])
students_descending = sorted(students, key = lambda student: student["score"], reverse = True)

print(students_ascending)
print(students_descending)

products = [
    {"name" : "Laptop", "price": 12000},
    {"name" : "iPhone", "price": 18000},
    {"name" : "Keyboard", "price": 2000},
    {"name" : "Mouse", "price": 1500}
]

sorted_products = sorted(products, key = lambda product: product["price"])
print(products)

people = [
    {"first_name" : "Martin", "last_name" : "Pettersson"},
    {"first_name" : "Anna", "last_name" : "Bengtsson"},
    {"first_name" : "John", "last_name" : "Smith"},
    {"first_name" : "Bob", "last_name" : "Charles"},
    {"first_name" : "John", "last_name" : "Tolkien"},
    {"first_name" : "Harry", "last_name" : "Potter"}
]

sorted_people = sorted(people, key = lambda person: person["last_name"])
print(sorted_people)

def sort_key(item):
    return len(item)

items = ["hello", "this", "is", "an", "item"]

sorted_items = sorted(items, key=sort_key)
print(sorted_items)

sorted_items_lambda = sorted(items, key=lambda item: len(item))
print(sorted_items_lambda)

# Part F

products = [
    {"name" : "   laptOp", "price": 12000, "category" : "computer", "stock": 10},
    {"name" : "   iphone  ", "price": 18000, "category" : "phone", "stock": 20},
    {"name" : "   desktop  ", "price": 14000, "category" : "computer", "stock": 32},
    {"name" : "   mp3    player  ", "price": 3000, "category" : "music player", "stock": 14},
    {"name" : "   mouse  ", "price": 500, "category" : "accesory", "stock": 0},
    {"name" : "keyboard  ", "price": 700, "category" : "accesory", "stock": 17},
    {"name" : "  headset  ", "price": 1200, "category" : "accesory", "stock": 25},
    {"name" : "piano  ", "price": 5000, "category" : "instrument", "stock": 53},
    {"name" : "     guitar", "price": 3000, "category" : "instrument", "stock": 0},
    {"name" : "   book", "price": 190, "category" : "book", "stock": 62},
    {"name" : "   flash   memory", "price": 600, "category" : "computer", "stock": 63},
    {"name" : "   monitor  ", "price": 4000, "category" : "accesory", "stock": 0}
]

products_dict = [{product["name"].strip().title() for product in products}]
print(products_dict)

in_stock = [product["name"].strip().title() for product in products if product["stock"] > 0]
print(in_stock)

categories = {product["category"] for product in products}
print(categories)

inventory_values = {product["name"].strip().title(): product["price"] * product["stock"] for product in products}
print(inventory_values)

print("----")

sorted_inventory = sorted(inventory_values.items(), key=lambda item: item[1])
print(sorted_inventory)

for i, item in enumerate(sorted_inventory, start=1):
    print(f"{i}. {item}")

prices = [product["price"] for product in products]
stock = [product["stock"] for product in products]
prices_and_stock = list(zip(prices, stock))
print(prices_and_stock)

names = [product["name"].strip().title() for product in products]
names_and_prices = list(zip(names, prices))
print(names_and_prices)

complicated = [product["price"] * 2 for product in products if len(product["name"]) > 3 and product["stock"] > 0]
print(complicated)

# Imo this looks clearer.
price_increased_products = []
for product in products:
    if product["stock"] > 0 and len(product["name"]) > 3:
        price_increased_products.append(product["price"]*2)
print(price_increased_products)

# Part G

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

flat = [value for row in matrix for value in row]
print(flat)

table = {
    row: {col: row * col for col in range(1, 11)}
    for row in range(1, 11)
}

print(table[3][7]) 

students = [
    {"name": "Martin", "score": 100},
    {"name": "Anna", "score": 20},
    {"name": "Sara", "score": 30},
    {"name": "Hilda", "score": 80},
    {"name": "Peter", "score": 70}
]

passing_students = {
    student["name"]: student["score"]
    for student in students
    if student["score"] >= 70
}

print(passing_students)

scores = [343,54,63,63,0,424,242,532,32]

print(all(scores))
print(any(scores))

scores = [0, 0, None]

print(all(scores))
print(any(scores))



