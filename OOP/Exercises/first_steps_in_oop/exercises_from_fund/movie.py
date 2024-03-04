class Movie:
    __watched_movies = 0

    def __init__(self, name: str, director: str):
        self.name = name
        self.director = director
        self.watched = False

    # Changes the name of the movie
    def change_name(self, new_game: str):
        self.name = new_game

    # Changes the director of the movie
    def change_director(self, new_director: str):
        self.director = new_director

    # Set the bool to True and increase the counter
    def watch(self):
        if not self.watched:
            self.watched = True
            Movie.__watched_movies += 1

    def __repr__(self):
        return f"Movie name: {self.name}; Movie director: {self.director}.Total watched movies: {Movie.__watched_movies}"


first_movie = Movie("Inception", "Christopher Nolan")
second_movie = Movie("The Matrix", "The Wachowskis")
third_movie = Movie("The Predator", "Shane Black")
first_movie.change_director("Me")
third_movie.change_name("My Movie")
first_movie.watch()
third_movie.watch()
first_movie.watch()
print(first_movie)
print(second_movie)
print(third_movie)
