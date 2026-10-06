# Part A

def part_a():
    num = float(input("Enter a number: "))
    if num > 0:
        print("Positive number")
    elif num < 0:
        print("Negative number")
    else:
        print("Zero")

    age = input("Enter your age: ")
    if age.isdigit():
        age = int(age)
        if age < 18:
            print("You are a minor.")
        elif age < 65:
            print("You are an adult.")
        else:
            print("You are a senior citizen.")

    username = "martin"
    password = "password123"
    input_username = input("Enter your username: ")
    input_password = input("Enter your password: ")
    if input_username == username and input_password == password:
        print("Login successful!")

    score = 78
    if score >= 90:
        print("Grade: A")
    elif score >= 80:
        print("Grade: B")
    elif score >= 70:
        print("Grade: C")
    elif score >= 60:
        print("Grade: D")
    else:
        print("Grade: F")

    member = True
    order_total = 120

    if member and order_total > 100:
        discount = 0.1
        print(f"Discount applied: {discount * 100}%")

    a = 5
    b = 3

    if a > b:
        print(f"{a} is greater than {b}")
    if a < b:
        print(f"{a} is less than {b}")
    if a == b:
        print(f"{a} is equal to {b}")
    if a != b:
        print(f"{a} is not equal to {b}")
    if a >= b:
        print(f"{a} is greater than or equal to {b}")
    if a <= b:
        print(f"{a} is less than or equal to {b}")


# Part B

def part_b():
    if "":
        print("This will not print because the string is empty.")
    if "Hello":
        print("This will print because the string is not empty.")
    if 0:
        print("This will not print because 0 is considered False.")
    if 3:
        print("This will print because 3 is considered True")
    if []:
        print("Will not print.")
    if [1,2,3]:
        print("This will print.")

    languages = ["Java", "C++", "Python"]
    if "Java" in languages:
        print("Java is a language in the list.")

    blocked_usernames = ["greg", "greta", "hans"]
    if "greg" in blocked_usernames:
        print("greg is a blocked username")

    roses_are_red = False
    violets_are_blue = False

    if not roses_are_red and not violets_are_blue:
        print("The garden will print.")


# Part C

def part_c():
    names = ["alice", "bob", "charles"]

    i = 1
    for name in names:
        print(f"Hello {name} {i}")
        i += 1

    for number in range(1, 51):
        if (number % 2 == 0):
            print(number)

    numbers = [123,532,523,2,5,2,243,24,45,6]

    sum = 0

    for number in numbers:
        sum += number
    print(sum)

    maximum = numbers[0]

    for number in numbers:
        if number >= maximum:
            maximum = number

    print(f"{maximum} is the maximum value in the list.")

    words = ["roses", "are", "red", "violets", "are", "blue"]

    count = 0
    for word in words:
        if len(word) > 5:
            count += 1

    print(f"{count} words have more than 5 characters.")

    scores = [90, 23, 43, 67, 89]

    count = 0
    threshold = 75
    for score in scores:
        if score >= threshold:
            count += 1
    print(f"{count} students passed.")

    # Example dictionary
    student = {
        "name": "Martin",
        "age": 20,
        "city": "Stockholm"
    }

    # 1. Loop over keys
    for key in student:
        print(key)

    # 2. Loop over values
    for value in student.values():
        print(value)

    # 3. Loop over key-value pairs
    for key, value in student.items():
        print(key, value)


# Part D

def part_d():
    # Fix: Use range to print 10 down to 1
    for i in range(10, 0, -1):
        print(i)

    number = input("Enter number for multiplication table: ")
    number = int(number)
    print(f"You entered {number}")

    result = 0
    for i in range(1, 11):
        result = i * number
        print(result)

    playlist = ["Song A", "Song B", "Song C", "Song D"]

    for track_number, song in enumerate(playlist, start=1):
        print(f"{track_number}. {song}")

    for x in range(4):
        for y in range(5):
            print(f"({x}, {y})")

    for row in range(5):
        for col in range(5):
            print("#", end=" ")
        print()


# Part E, While loops

def part_e():
    countdown = 10
    while countdown >= 0:
        print(countdown)
        countdown -= 1

    correct_password = "pass"
    password = ""
    while password != correct_password:
        password = input("Enter a password: ")

    quit = False

    while not quit:
        print("1. Spaghetti Carbonara")
        print("2. Pizza Margherita")
        print("3. Meatballs")
        print("4. Quit")
        choice = input("Enter choice: ")
        choice = int(choice)
        if choice == 1:
            print("Carbonara")
        elif choice == 2:
            print("Margherita")
        elif choice == 3:
            print("Meatballs")
        elif choice == 4:
            print("Good bye")
            quit = True
        else:
            continue

    input_number = 1
    total = 0
    while input_number != 0:
        input_number = int(input("Enter a number: "))
        total += input_number
        print(f"Total: {total}")

    secret_number = 67
    guess = 0
    while guess != secret_number:
        guess = int(input("Guess a number: "))
        if guess > secret_number:
            print("Too high.")
        else:
            print("Too low")
    print("Correct!")

    for i in range(1, 101):
        if i % 7 == 0 and i % 9 == 0:
            print(i)
            break

    strings = ["lol", "", "avada", "kedavra", "sixseven", "", "Java"]
    for str in strings:
        if str == "":
            continue
        else:
            print(str)

    target = "sixseven"
    for str in strings:
        if str == target:
            print("Found")
            break

    numbers = [-23,32,532,62,-32124,432,999]
    for num in numbers:
        if num < 0:
            continue
        elif num == 999:
            break


# Part F, Console study tracker

def part_f():
    courses = [{"subject" : "Java", "minutes" : 56}, {"subject" : "Python", "minutes" : 34}, {"subject" : "C++", "minutes" : 234}]

    total_minutes = 0
    for course in courses:
        total_minutes += course["minutes"]
    print(total_minutes)

    courses = []
    total_minutes = 0
    while(True):
        subject = input("Enter subject: ")
        minutes = int(input("Enter minutes: "))
        dict = {"subject" : subject, "minutes" : minutes}
        courses.append(dict)
        for course in courses:
            total_minutes += course["minutes"]
        print(f"Total minutes: {total_minutes}")
        exit = input("Exit? ")
        if exit == "y":
            break

    courses = [{"subject" : "Java", "minutes" : 56}, 
            {"subject" : "Python", "minutes" : 34}, 
            {"subject" : "C++", "minutes" : 234},
            {"subject" : "Assembly", "minutes" : 56}, 
            {"subject" : "Rust", "minutes" : 34}, 
            {"subject" : "C", "minutes" : 234},
            {"subject" : "Perl", "minutes" : 56}, 
            {"subject" : "Ruby", "minutes" : 34}, 
            {"subject" : "JavaScript", "minutes" : 234}
            ]
    longest_minutes = courses[0]["minutes"]

    for course in courses:
        if course["minutes"] > longest_minutes:
            longest_minutes = course["minutes"]

    print(f"Longest course: {longest_minutes}")

    for course in courses:
        if course["minutes"] > 45:
            print(course["subject"])

    while(True):
        print("1. View all sessions")
        print("2. View total time")
        print("3. Filter by subject")
        print("4. Quit")
        choice = int(input(">>> "))
        if choice == 1:
            for course in courses:
                print(course["subject"])
        elif choice == 2:
            total = 0
            for course in courses:
                total += course["minutes"]
            print(f"Total time: {total}")
        elif choice == 3:
            subject = input("Enter subject: ")
            filter = []
            for course in courses:
                if course["subject"] == subject:
                    filter.append(course)
            for course in filter:
                print(course)
        elif choice == 4:
            break
        else:
            continue


# Part G, Stretch challenges

def part_g():
    for i in range(101):
        if i % 3 == 0 and i % 5 == 0:
            print(f"FizzBuzz: {i}")
        elif i % 3 == 0:
            print(f"Fizz: {i}")
        elif i % 5 == 0:
            print(f"Buzz: {i}")
        else:
            continue

    vowels = ["a", "i", "u", "e", "o"]
    sentence = "Roses are red, violets are blue"

    count = 0
    for char in sentence:
        if char in vowels:
            count += 1
    print(f"Vowels: {count}")

    nums = [234,43,5,33,2,2,2,2,4324,64,234,2]
    dict = {}
    for num in nums:
        if num in dict:
            dict[num] += 1
        else:
            dict[num] = 1
    print(dict)

    nums = [3, 5, 2]

    for num in nums:
        print("*"*num)


# Main program

if __name__ == "__main__":
    part_a()
    part_b()
    part_c()
    part_d()
    part_e()
    part_f()
    part_g()