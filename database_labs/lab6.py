from pprint import pprint
from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

for product in db.products.find(
    {"category": "Accessories"},
    {"name": 1, "_id": 0}
):
    print(product["name"])

print("\n")

for customer in db.customers.find(
    {"city": "Göteborg"},
    {"first_name": 1, "last_name": 1, "_id": 0}
):
    print(customer["first_name"], customer["last_name"])

print("\n")

for product in db.products.find():
    print(product["name"], product["price"])

print("\n")

uppsala_count = db.customers.count_documents({"city": "Uppsala"})
print("Number of customers in Uppsala:", uppsala_count)

print("\n")

sandals = db.products.find_one({"name": "Sandals"})
if sandals:
    print("Sandals stock:", sandals["stock"])
else:
    print("Sandals not found in the database.")

print("\n")

for customer in db.customers.find({"newsletter": True}):
    print(customer["first_name"])

print("\n")

db.customers.insert_one({"first_name": "Martin", "last_name": "Pettersson", "email": "martin.pettersson@example.com"})

martin = db.customers.find_one({"first_name": "Martin", "last_name": "Pettersson"})
print("Martin's id:", martin["_id"])
martin = db.customers.find_one({"email": "martin.pettersson@example.com"})
pprint(martin)

print("\n")

db.products.insert_many([
    {"id": 13, "name": "Beanie Red", "category": "Accessories", "price": 199, "stock": 15, "tags": ["winter"], "details": {"color": "red", "material": "wool"}},
    {"id": 14, "name": "Beanie Blue", "category": "Accessories", "price": 199, "stock": 20, "tags": ["winter"], "details": {"color": "blue", "material": "wool"}}])

products_count = db.products.count_documents({})
print(products_count)

print("\n")

for customer in db.customers.find(
    {},
    {"first_name": 1, "last_name": 1, "city": 1, "_id": 0}
):
    print(f"{customer.get('first_name', '')} {customer.get('last_name', '')} ({customer.get('city', '')})")

print("\n")

for order_number, order in enumerate(db.orders.find(), start=1):
    item_count = len(order.get("items", []))
    print(f"Order {order_number}: {item_count} items")
