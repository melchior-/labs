from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

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

@app.post("/movies", status_code=201)
def create_movie(movie: Movie):
    new_id = max((m["id"] for m in movies), default=0) + 1
    new_movie = {"id": new_id, "title": movie.title, "director": movie.director, "year": movie.year}
    movies.append(new_movie)
    return new_movie

@app.put("/movies/{movie_id}")
def replace_movie(movie_id: int, movie: Movie):
    existing = find_movie(movie_id)
    existing["title"] = movie.title
    existing["director"] = movie.director
    existing["year"] = movie.year
    return existing

@app.delete("/movies/{movie_id}", status_code=204)
def delete_movie(movie_id: int):
    movie = find_movie(movie_id)
    movies.remove(movie)
    return {"message": "Movie deleted successfully"}

class MovieUpdate(BaseModel):
    title: str | None = None
    director: str | None = None
    year: int | None = None

@app.patch("/movies/{movie_id}")
def update_movie(movie_id: int, movie_update: MovieUpdate):
    existing = find_movie(movie_id)
    if movie_update.title is not None:
        existing["title"] = movie_update.title
    if movie_update.director is not None:
        existing["director"] = movie_update.director
    if movie_update.year is not None:
        existing["year"] = movie_update.year
    return existing






