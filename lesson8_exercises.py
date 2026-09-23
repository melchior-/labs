# Part A

class BadTeam():

    def __init__(self, name, members = []):
        self.name = name
        self.members = members

    def add_member(self, new_member):
        self.members.append(new_member)

team1 = BadTeam("Hawks")
team2 = BadTeam("Lions")

team1.add_member("Martin")

print(team1.members)
print(team2.members)

# The member gets added to both teams. memers=[] is a default argument, and Python creates that list once when the function is defined, not once per instance.

class Team():
    def __init__(self, name, members = None):
        self.name = name
        self.members = [] if members is None else members

    def add_member(self, new_member):
        self.members.append(new_member)

team1 = Team("Hawks")
team2 = Team("Lions")

team1.add_member("Martin")

print(team1.members)
print(team2.members)

# Part B

movie_dict = {"title" : "Forrest Gump", "director" : "Robert Zemeckis", "rating" : 8.0}

class Movie():
    def __init__(self, title, director, rating):
        self.title = title
        self.director = director
        self.rating = rating

    def is_highly_rated(self):
        if self.rating >= 7.9:
            return True
        return False

# I would choose the dictionary if there is no behavior needed for the movies or repeated objects. If we need validation or logic to be used on the movies I would choose a class.

