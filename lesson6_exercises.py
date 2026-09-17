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

dict = {product["name"]: product["price"] for product in products if product["price"] <= threshold}

print(dict)

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





