# Part A

def part_a():
    languages = ["Python", "JavaScript", "C++", "Java", "Ruby", "Go", 
                 "Swift", "Kotlin", "PHP", "TypeScript"]
    first_language = languages[0]
    last_language = languages[-1]
    third_language = languages[2]
    second_to_last_language = languages[-2]

    print(languages[3:6])
    print(languages[::2])
    print(languages[::-1])

    languages.append("Rust")
    print(languages)
    languages.insert(2, "C#")
    print(languages)
    languages.remove("Java")
    print(languages)
    languages.pop(4)
    print(languages)

    nums = [10, 20, 30, 40, 50]
    length = len(nums)
    min_ = min(nums)
    max_ = max(nums)
    sum_ = sum(nums)

    nums1 = [432, 532, 234, 52, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    nums2 = sorted(nums1, reverse=True)
    nums1.sort()
    print(nums1)
    print(nums2)

    list_a = [1, 2, 3]
    list_b = [4, 5, 6]
    list_a = list_b
    # We need to use .copy to create a new list that is a copy of list_b, 
    # so that changes to list_a do not affect list_b.
    list_c = list_b.copy()


# Part B, Tuples and Unpacking

def part_b():
    rgb = (255, 0, 0)
    red = rgb[0]
    green = rgb[1]
    blue = rgb[2]
    print(f"Red: {red}, Green: {green}, Blue: {blue}")

    person = ("Martin", "Stockholm", 35)
    name, city, age = person
    print(f"Name: {name}, City: {city}, Age: {age}")

    # We cannot change the values of a tuple, but we can create a 
    # new tuple with the desired values.
    # This is useful when we want to update the values of a 
    # tuple without changing the original tuple.

    list_of_tuples = [("Python", 3.9), ("Java", 15), ("C++", 11)]
    for tuple in list_of_tuples:
        language, version = tuple
        print(f"Language: {language}, Version: {version}")


# Part C, Sets

def part_c():
    list_of_courses = ["Python", "Java", "C++", "Python", "JavaScript", "Java"]
    set_of_courses = set(list_of_courses)
    print(len(list_of_courses))
    print(len(set_of_courses))

    skills1 = {"coding", "music", "maths", "machine learning", "building"}
    skills2 = {"coding", "working", "music"}
    shared_skills = skills1.intersection(skills2)

    skills2.add("maths")
    skills1.remove("building")
    includes = "maths" in skills1

    print(f"Shared skills: {shared_skills}")

    # Sometimes a set is a better choice than a list because it is faster
    # to check if an item is in a set than in a list.


# Part D, Dictionaries

def part_d():
    laptop = {
        "brand": "Dell",
        "model": "XPS 13",
        "year": 2022,
        "specs": {
            "CPU": "Intel Core i7",
            "RAM": "16GB",
            "Storage": "512GB SSD"
        },
        "price": 1499.99
    }

    laptop["price"] = 1399.99
    laptop.update({"operating_system": "Windows 11"})

    os = laptop.get("operating_system")
    shiny = laptop.get("shiny", "Not found")

    for item in laptop.items():
        print(f"{item[0]}: {item[1]}")

    courses = {
        "Python": 3.9,
        "Java": 15,
        "C++": 11
    }

    total_hours = sum(courses.values())


# Part E, Nested collections

def part_e():
    list_of_dicts = [
        {"title": "Python Basics", "author": "John Doe", "pages": 250, "available": True},
        {"title": "Java Programming", "author": "Jane Smith", "pages": 300, "available": False},
        {"title": "C++ Fundamentals", "author": "Bob Johnson", "pages": 200, "available": True},
        {"title": "JavaScript Essentials", "author": "Alice Brown", "pages": 150, "available": True},
        {"title": "Ruby on Rails", "author": "Charlie Davis", "pages": 400, "available": False}
    ]

    title_third_book = list_of_dicts[2]["title"]
    available_last_book = list_of_dicts[-1]["available"]

    list_of_dicts[1].update({"color": "blue"})
    list_of_dicts[3]["available"] = False

    departments = {
        "HR": ["Alice", "Bob", "Charlie"],
        "IT": ["David", "Eva", "Frank"],
        "Finance": ["Grace", "Hannah", "Ian"]
    }

    courses = {
        "Python": {"instructor": "John Doe", "duration": 10, 
                   "topics": ["variables", "loops", "functions"]},
        "Java": {"instructor": "Jane Smith", "duration": 15, 
                 "topics": ["classes", "objects", "inheritance"]},
        "C++": {"instructor": "Bob Johnson", "duration": 12, 
                "topics": ["pointers", "memory management", "templates"]}
    }

    print(f"Topic of Python course: {courses['Python']['topics'][0]}")



# Part F, Personal Media Catalogue

def part_f():
    movies = [
        {"title": "Inception", "director": "Christopher Nolan", 
         "year": 2010, "genre": "Sci-Fi", "rating": 8.8},
        {"title": "The Dark Knight", "director": "Christopher Nolan", 
         "year": 2008, "genre": "Action", "rating": 9.0},
        {"title": "Interstellar", "director": "Christopher Nolan", 
         "year": 2014, "genre": "Sci-Fi", "rating": 8.6},
        {"title": "The Matrix", "director": "Lana Wachowski, Lilly Wachowski", 
         "year": 1999, "genre": "Sci-Fi", "rating": 8.7},
         {"title": "The Godfather", "director": "Francis Ford Coppola", 
          "year": 1972, "genre": "Crime", "rating": 9.2},
        {"title": "Pulp Fiction", "director": "Quentin Tarantino", 
         "year": 1994, "genre": "Crime", "rating": 8.9},
        {"title": "The Shawshank Redemption", "director": "Frank Darabont", 
         "year": 1994, "genre": "Drama", "rating": 9.3},
        {"title": "The Lord of the Rings: The Return of the King", "director": "Peter Jackson", 
         "year": 2003, "genre": "Fantasy", "rating": 8.9},
        {"title": "Forrest Gump", "director": "Robert Zemeckis", 
         "year": 1994, "genre": "Drama", "rating": 8.8},
        {"title": "Fight Club", "director": "David Fincher", 
         "year": 1999, "genre": "Drama", "rating": 8.8}
    ]

    set_of_genres = set()
    for movie in movies:
        set_of_genres.add(movie["genre"])

    print(f"Unique genres in the movie collection: {set_of_genres}")

    tuple_title_and_year = [(movie["title"], movie["year"]) for movie in movies]
    print(f"Title and year of each movie: {tuple_title_and_year}")

    genres = [movie["genre"] for movie in movies]
    years = [movie["year"] for movie in movies]
    titles = [movie["title"] for movie in movies]
    ratings = [movie["rating"] for movie in movies]
    directors = [movie["director"] for movie in movies]
    movies[0]["rating"] = 9.0
    print(f"Updated rating for {movies[0]['title']}: {movies[0]['rating']}")
    movies[1]["director"] = "Nolan"
    print(f"Updated director for {movies[1]['title']}: {movies[1]['director']}")
    movies[2]["year"] = 2015
    print(f"Updated year for {movies[2]['title']}: {movies[2]['year']}")
    movies[3]["genre"] = "Action"
    print(f"Updated genre for {movies[3]['title']}: {movies[3]['genre']}")
    movies[4]["title"] = "The Godfather Part I"
    print(f"Updated title for movie 5: {movies[4]['title']}")

    # Summary of catalogue:
    print(f"Total movies in collection: {len(movies)}")
    # All movie titles in the collection:
    all_titles = [movie["title"] for movie in movies]
    print(f"All movie titles in the collection: {all_titles}")


# Part G, Challenges

def part_g():
    usernames1 = ["alice", "bob", "charlie", "david", "eve"]
    usernames2 = ["bob", "grace", "eve", "ivan", "judy"]

    duplicate_usernames = set(usernames1).intersection(set(usernames2))
    print(f"Duplicate usernames: {duplicate_usernames}")

    unique_usernames = set(usernames1).union(set(usernames2))
    print(f"Unique usernames: {unique_usernames}")

    course_platform = {
        "Python": {"instructor": "John Doe", "duration": 10, "students": 100},
        "JavaScript": {"instructor": "Jane Smith", "duration": 8, "students": 80},
        "Java": {"instructor": "Bob Johnson", "duration": 12, "students": 120},
        "Students": {"Alice": {"age": 25, "city": "New York"},
                     "Bob": {"age": 30, "city": "Los Angeles"},
                     "Charlie": {"age": 28, "city": "Chicago"}},
        "Topics": ["variables", "loops", "functions", "classes", "objects"]
    }

    inventory = {
        "apples": {"quantity": 50, "price_per_unit": 0.5},
        "bananas": {"quantity": 30, "price_per_unit": 0.3},
        "oranges": {"quantity": 20, "price_per_unit": 0.4},
        "grapes": {"quantity": 15, "price_per_unit": 0.6}
    }

    total_quantity = sum(item["quantity"] for item in inventory.values())
    total_value = sum(item["quantity"] * item["price_per_unit"] for item in inventory.values())
    inventory["bananas"]["quantity"] += 10

    # Comparison of list, tuples, sets, and dictionaries
    # Lists are ordered, mutable, and allow duplicate elements.
    # Tuples are ordered, immutable, and allow duplicate elements.
    # Sets are unordered, mutable, and do not allow duplicate elements.
    # Dictionaries are unordered, mutable, and store key-value pairs.


# Main program

if __name__ == "__main__":
    part_a()
    part_b()
    part_c()
    part_d()
    part_e()
    part_f()
    part_g()