class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author 
        self.pages = pages

book1 = Book("A Dance with Dragons", "George RR Martin", 1100)
book2 = Book("Frankenstein", "Mary Shelley", 400)
book3 = Book("Red Rising", "Pierce Brown", 350)
book4 = Book("Angels and Demons", "Dan Brown", 500)

print(book1.title)
print(book1.author)
print(book1.pages)

class Laptop():
    def __init__(self, brand, model, ram_gb, price):
        self.brand = brand
        self.model = model
        self.ram_gb = ram_gb
        self.price = price

laptop1 = Laptop("Dell", "XPS", 16, 8000)
laptop2 = Laptop("HP", "Pavilion", 32, 10000)
laptop3 = Laptop("Apple", "MacBook", 128, 21000)

laptop3.price = 18000