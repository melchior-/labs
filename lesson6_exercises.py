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