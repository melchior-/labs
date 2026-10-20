from api_client import get_json
import requests

BASE = "http://127.0.0.1:8000"

books = get_json(f"{BASE}/books")

print(books)

new_book = {"title": "Snow Crash", "author": "Neal Stephenson", "year": 1992}
response = requests.post(f"{BASE}/books", json=new_book)
print(response.status_code, response.json())

get_json(f"{BASE}/books/99")  # This should return a 404 error
