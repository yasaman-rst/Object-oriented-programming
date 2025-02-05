class Movie:
    def __init__(self, name, director, genre, year):
        self.name = name
        self.director = director
        self.genre = genre
        self.year = year

# Function to filter movies by genre
def movies_of_genre(movies, genre):
    return list(filter(lambda movie: movie.genre == genre, movies))


# Creating movie objects
john_woo = Movie("A Better Tomorrow", "John Woo", "action", 1986)
kungfu = Movie("Chinese Odyssey", "Stephen Chow", "comedy", 1993)
jet_li = Movie("The Legend", "Corey Yuen", "comedy", 1993)
hero = Movie("Hero", "Yimou Zhang", "action", 2002)

movies = [john_woo, kungfu, jet_li, hero]
print("Movies in the action genre:")
for movie in movies_of_genre(movies, "action"):
    print(f"{movie.director}: {movie.name}")

# Ref:https://www.guvi.in/hub/python/filtering-a-list-using-the-filter()-method-in-python/#:~:text=Syntax%20for%20filter()%20Function%20in%20Python%3A,-The%20syntax%20for&text='filter'%3A%20This%20is%20the,function%2C%20or%20a%20lambda%20function.