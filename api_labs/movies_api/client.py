from api_client import get_json
import requests

BASE = "http://localhost:8000"

movies = get_json(f"{BASE}/movies")
print(movies)
get_json(f"{BASE}/movies/99")  # This should return a 404 error

new_movie = {"title": "Inception", "director": "Christopher Nolan", "year": 2010}
response = requests.post(f"{BASE}/movies", json=new_movie)
print(response.json())
