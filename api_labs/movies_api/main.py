import json
import os

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel

app = FastAPI()

load_dotenv()  # Load environment variables from .env file
#api_key = os.getenv("API_KEY")  # Get the API key from environment variables API key from environment variables
api_key = "3b3705f7b65ee8441272077ef1a5be42" # Loading the API key directly from the .env file for testing purposes
print(f"Loaded API key: {api_key}")  # Print the loaded API key for debugging purposes

def check_key(provided_key: str):
    if provided_key != api_key:
        raise HTTPException(status_code=403, detail="Invalid API key")

def find_movie(movie_id: int):
    for movie in movies:
        if movie["id"] == movie_id:
            return movie
    raise HTTPException(status_code=404, detail="Movie not found")

@app.get("/")
def home():
    return {"message": "Hello World!"}

movies = [
    {"id": 1, "title": "The Shawshank Redemption", "director": "Frank Darabont", "year": 1994},
    {"id": 2, "title": "The Godfather", "director": "Francis Ford Coppola", "year": 1972},
    {"id": 3, "title": "The Dark Knight", "director": "Christopher Nolan", "year": 2008},
    {"id": 4, "title": "Pulp Fiction", "director": "Quentin Tarantino", "year": 1994}]

def load_movies():
    global movies
    with open("movies.json", "r") as f:
        movies = json.load(f)

load_movies()  # Load movies from the JSON file at startup

print(f"Loaded {len(movies)} movies from movies.json")  # Print the number of loaded movies for debugging purposes

def save_movies():
    with open("movies.json", "w") as f:
        json.dump(movies, f)

save_movies()  # Save movies to the JSON file at startup

@app.get("/movies")
def get_movies(director: str = None):
    if director:
        return [movie for movie in movies if director.lower() in movie["director"].lower()]
    return movies

@app.get("/movies/{movie_id}")
def get_movie(movie_id: int):
    return find_movie(movie_id)

@app.get("/movies")
def get_movies(director: str | None = None, year: int | None = None):
    return [
        movie for movie in movies
        if (director is None or director.lower() in movie["director"].lower())
        and (year is None or movie["year"] == year)
    ]

class Movie(BaseModel):
    title: str
    director: str
    year: int

@app.post("/movies", status_code=201, dependencies=[Depends(check_key)])
def create_movie(movie: Movie):
    new_id = max((m["id"] for m in movies), default=0) + 1
    new_movie = {"id": new_id, "title": movie.title, "director": movie.director, "year": movie.year}
    movies.append(new_movie)
    save_movies()  # Save the updated movies list to the JSON file
    return new_movie

@app.put("/movies/{movie_id}", dependencies=[Depends(check_key)])
def replace_movie(movie_id: int, movie: Movie):
    existing = find_movie(movie_id)
    existing["title"] = movie.title
    existing["director"] = movie.director
    existing["year"] = movie.year
    save_movies()  # Save the updated movies list to the JSON file
    return existing

@app.delete("/movies/{movie_id}", status_code=204, dependencies=[Depends(check_key)])
def delete_movie(movie_id: int):
    movie = find_movie(movie_id)
    movies.remove(movie)
    save_movies()  # Save the updated movies list to the JSON file
    return {"message": "Movie deleted successfully"}

class MovieUpdate(BaseModel):
    title: str | None = None
    director: str | None = None
    year: int | None = None

@app.patch("/movies/{movie_id}", dependencies=[Depends(check_key)])
def update_movie(movie_id: int, movie_update: MovieUpdate):
    existing = find_movie(movie_id)
    if movie_update.title is not None:
        existing["title"] = movie_update.title
    if movie_update.director is not None:
        existing["director"] = movie_update.director
    if movie_update.year is not None:
        existing["year"] = movie_update.year
    save_movies()  # Save the updated movies list to the JSON file
    return existing

# PUT is used to replace the entire resource, while PATCH is used to update only specific fields of the resource.




