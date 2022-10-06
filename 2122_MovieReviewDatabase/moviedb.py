# COMP 1026 â€“ Assignment 4

# Dada Nguyen

# Write a program using data structures, functions and reading data from a file to simulate a preferential voting system.

from movie import Movie

class Moviedb:

    # constructor
    def __init__(self):
        self.database = {}

    # Create a new movie object and add it to the database
    def addMovie(self, title: str, year: int):
        try:
            (title, year) not in self.database
            self.database[(title, year)] = Movie(title, year)
        except KeyError:
            print('The movie {} is already in the database'.format(title))

    # Return the movie object in the database with the same name and year
    def findMovie(self, title: str, year: int) -> Movie:
        if (title, year) in self.database:
            return self.database[(title, year)]

    # Print all short reviews for all movies in the database
    def showAll(self):
        info = []
        for key in self.database:
            info.append((key[0], key[1]))

        info.sort()
        for (title,year) in info:
            print(self.database[(title, year)].shortReview())


# test here
if __name__ == "__main__":
    db = Moviedb()

    db.addMovie("LOL", 2000)
    db.addMovie('Kyber', 2021)
    db.showAll()