# COMP 1026 â€“ Assignment 4

# Dada Nguyen

# Write a program using data structures, functions and reading data from a file to simulate a preferential voting system.

class Movie:

    # Constructor
    def __init__(self, title: str, year: int):
        self.__title = title
        self.__year = year
        self.__reviews = {
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0
        }

    # Find Error
    def addReview(self, star: int):
        if star < 1 or star > 5:
            return
        self.__reviews[star] += 1

    # Representations
    def shortReview(self) -> str:
        shortReview: str = '{} ({}): {}/5'.format(self.__title, self.__year, self.__calcAverage())
        return shortReview

    def longReview(self) -> str:
        longReview: str = '{} ({})'.format(self.__title, self.__year) + '\n' + 'Average review: {}/5'.format(
            self.__calcAverage())
        for numStars in range(5, 0, -1):
            starDetail: str = ''
            for _ in range(0, numStars):
                starDetail += '*'
            for _ in range(numStars, 5):
                starDetail += ' '
            starDetail += ': ' + str(self.__reviews[numStars])
            longReview = longReview + '\n' + starDetail

        return longReview

    # Accessors
    def getTitle(self) -> str:
        return self.__title

    def getYear(self) -> int:
        return self.__year

    def __calcAverage(self) -> float:
        totalStar: int = 0
        numReviews: int = 0
        for star in range(1, 6):
            totalStar += star * self.__reviews[star]
            numReviews += self.__reviews[star]

        if numReviews == 0:
            return 0.0

        res: float = totalStar / numReviews
        return round(res, 1)


# test here
if __name__ == "__main__":
    kyber: Movie = Movie("star war", 2001)
    kyber.addReview(1)
    print(kyber.longReview())