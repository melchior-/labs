import datetime

from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

for product in db.products.find(
    {"price": {"$gt": 1000}},
    {"name": 1, "price": 1, "_id": 0}
):
    print(f"Product: {product['name']}, Price: {product['price']}")

print("\n")

for order in db.orders.find(
    {"status": {"$ne": "delivered"}},
    {"_id": 1, "customer_id": 1, "status": 1}
):
    print("Order ID:", order["_id"], "Customer ID:", order["customer_id"], "Status:", order["status"])

print("\n")

for customers in db.customers.find(
    {"city": {"$in": ["Stockholm", "Malmö"]}},
    {"first_name": 1, "last_name": 1, "city": 1, "_id": 0}
):
    print("Customer:", customers["first_name"], customers["last_name"], "City:", customers["city"])

print("\n")

for products in db.products.find(
    {"details.color": "white"},
    {"name":1, "details.color": 1, "_id": 0}
):
    print("Product:", products["name"], "Color:", products["details"]["color"]) 

print("\n")

for product in db.products.find(
    {"tags": "sport"},
    {"name": 1, "tags": 1, "_id": 0}
):
    print("Product:", product["name"], "Tags:", product["tags"] )

print("\n")

for products in db.products.find(
    {},
    {"name": 1, "price": 1, "_id": 0}
).sort("price", 1).limit(5):
    print("Product:", products["name"], "Price:", products["price"])

print("\n")

for order in db.orders.find(
    {"items.name": "T-shirt White", "items.quantity": 2},
    {"_id": 1, "customer_id": 1, "items": 1}
):
    print("Order ID:", order["_id"], "Customer ID:", order["customer_id"], "Items:", order["items"])

print("\n")

result = db.products.update_many(
    {"category": "Accessories"},
    {"$inc": {"price": 20}}
)

print("Number of products updated:", result.modified_count)

print("\n")

today = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)

result = db.products.update_one(
    {"name": "Rain Jacket"},
    {
        "$addToSet": {"tags": "new"},
        "$set": {"restock_date": today}
    }
)

print("Rain Jacket found:", result.matched_count == 1)

print("\n")

cutoff = datetime.datetime(2026, 3, 20)

result = db.orders.delete_many({
    "status": "new",
    "order_date": {"$lt": cutoff}
})

print("Orders deleted:", result.deleted_count)
