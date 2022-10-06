# COMP 1026 â€“ Assignment 4

# Dada Nguyen

# Write a program using data structures, functions and reading data from a file to simulate a preferential voting system.

from moviedb import Moviedb

COMMAND = 0
TITLE = 1
YEAR = 2
REVIEW = 3

NEW_COMMAND = 'NEW'
REVIEW_COMMAND = 'REV'
SHOW_COMMAND = 'SHO'
PRINT_COMMAND = 'PRI'


def readFile(inputFile):
    db = Moviedb()
    with open(inputFile, 'r') as fh:
        for line in fh:
            data = line.strip().split('-')

            command = data[COMMAND]

            # PROCESSING NEW COMMANDS
            if command == NEW_COMMAND:
                title = data[TITLE]
                year = int(data[YEAR])
                db.addMovie(title, year)

            # PROCESSING REV COMMANDS
            elif command == REVIEW_COMMAND:
                title = data[TITLE]
                year = int(data[YEAR])
                star = int(data[REVIEW])
                if db.findMovie(title, year) is not None:
                    db.findMovie(title, year).addReview(star)

            # PROCESSING SHO COMMANDS
            elif command == SHOW_COMMAND:
                db.showAll()

            # PROCESSING PRI COMMANDS
            elif command == PRINT_COMMAND:
                title = data[TITLE]
                year = int(data[YEAR])
                if db.findMovie(title, year) is not None:
                    print(db.findMovie(title, year).longReview())


def main():
    inputFile = input('Enter the name of the file: ')
    readFile(inputFile)


# test here
if __name__ == '__main__':
    main()