def movie_organizer(*films_info):
    movies = {}

    # Separate each film on base its genre
    for title, genre in films_info:
        if genre not in movies:
            movies[genre] = []
        movies[genre].append(title)

    # Initialise a variable for the return
    result = []

    # Sort the dictionary and append messages to the result
    sorted_tuple = sorted(movies.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))
    for genre, movies in sorted_tuple:
        result.append(f"{genre} - {len(movies)}")
        sorted_movies = sorted(movies, key=lambda kvp: kvp)

        for movie in sorted_movies:
            result.append(f'* {movie}')

    return '\n'.join(result)


print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))
