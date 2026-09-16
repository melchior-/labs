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