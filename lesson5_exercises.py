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




    