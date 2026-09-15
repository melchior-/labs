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

