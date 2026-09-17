# ==================================================
# TASK 1
# ==================================================

products = [
    {"name": "Laptop", "price": 12000, "stock": 4},
    {"name": "Mouse", "price": 350, "stock": 0},
    {"name": "Keyboard", "price": 800, "stock": 6},
    {"name": "Monitor", "price": 3200, "stock": 3},
    {"name": "Headset", "price": 950, "stock": 0},
    {"name": "Webcam", "price": 1100, "stock": 5}
]

# 1. Loop through the products.
# 2. Print the name of every product that is in stock.
# 3. Calculate the total value of all products in stock.
#    The value of a product is price * stock.
# 4. Print the total value.
# 5. Keep track of which in-stock product has the highest price
#    without using max(), and print its name.


# Write your solution below:

#1

for product in products:
    print(product)

#2

for product in products:
    if product["stock"] > 0:
        print(product["name"])

#3

total_value = 0
for product in products:
    value = product["price"] * product["stock"]
    total_value += value

#4

print(total_value)

#5
max_price = 0
max_name = ""
for product in products:
    if product["stock"] > 0:
        price = product["price"]
        if price > max_price:
            max_price = price
            max_name = product["name"]
print(max_name)


# ==================================================
# TASK 2
# ==================================================

scores = [78, 92, 55, 81, 67, 95, 73]

# Create a function called calculate_average that:
# - receives a list of scores
# - calculates and returns the average score
#
# Create another function called create_result that:
# - receives a list of scores
# - uses calculate_average()
# - returns "PASS" if the average is 70 or higher
# - otherwise returns "FAIL"
#
# Call create_result() using the scores above.
# Print both the average score and the final result.


# Write your solution below:

def calculate_average(scores):
    total_score = 0
    for score in scores:
        total_score += score
    average = total_score / len(scores)
    return average

def create_result(scores):
    average = calculate_average(scores)
    if average > 70:
        return "PASS"
    else:
        return "FAIL"

average = calculate_average(scores)
print(average)
result = create_result(scores)
print(result)


# ==================================================
# TASK 3
# ==================================================

product_prices = [250, 400, 150, 700]

order_settings = {
    "discount": 10,
    "shipping": 49,
    "priority": True
}

# Create a function called calculate_order that:
# - receives a customer name as a normal parameter
# - receives any number of product prices using *args
# - receives optional settings using **kwargs
# - calculates the subtotal of all product prices
# - applies the discount percentage if "discount" exists
# - adds shipping if "shipping" exists
# - returns a dictionary containing:
#       customer
#       subtotal
#       final_total
#       settings
#
# Call the function using:
# - customer name "Anna"
# - the values from product_prices using unpacking
# - the values from order_settings using dictionary unpacking
#
# Print the returned dictionary.


# Write your solution below:

def calculate_order(name, *product_prices, **settings):
    subtotal = 0
    for price in product_prices:
        subtotal += price
    discount_percentage = 0
    if "discount" in settings:
        discount_percentage = settings["discount"]
    fee = 0
    if "shipping" in settings:
        fee = settings["shipping"]
    disc = (100 - discount_percentage) / 100
    final_total = subtotal * disc + fee

    return_dict = {}
    return_dict["customer"] = name
    return_dict["subtotal"] = subtotal
    return_dict["final_total"] = final_total

    for key, value in settings.items():
        return_dict[key] = value

    return return_dict

order_dict = calculate_order("Anna", *product_prices, **order_settings)
print(order_dict)



# ==================================================
# TASK 4
# ==================================================

players = [
    {"name": "  anna", "score": 85, "active": True},
    {"name": "DAVID ", "score": 72, "active": False},
    {"name": " sara ", "score": 94, "active": True},
    {"name": "LEO", "score": 67, "active": True},
    {"name": " emma", "score": 88, "active": True},
    {"name": "OSCAR ", "score": 76, "active": False}
]

# 1. Create a new list containing normalized player names.
#    Remove unnecessary whitespace and use consistent capitalization.
#    Use a list comprehension.
#
# 2. Create a new list containing only the active players
#    with a score of 80 or higher.
#    Use a list comprehension.
#
# 3. Sort the original players by score from highest to lowest.
#    Use sorted() with a lambda.
#
# 4. Print the ranking in the following format:
#
#    1. Sara - 94
#    2. Emma - 88
#    ...
#
#    Generate the ranking numbers using enumerate().
#
# 5. Create a separate list containing the player names and
#    another list containing their scores.
#    Combine them using zip() and print each name together
#    with its score.


# Write your solution below:

#1

names = [player["name"].strip().capitalize() for player in players]
print(names)

#2

active = [player["name"].strip().capitalize() for player in players if player["score"] >= 80]
print(active)

#3

result = sorted(players, key = lambda player : player["score"], reverse = True)
print(result)

#4

for i, player in enumerate(result, start=1):
    print(f"{i}. {player["name"].strip().capitalize()} - {player["score"]}")

#5

names = [player["name"].strip().capitalize() for player in players]
scores = [player["score"] for player in players]
combined = zip(names, scores)
for element in combined:
    print(element)