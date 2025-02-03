from data import movies
# 1

def is_above_5_5(movie):
    return movie["imdb"] > 5.5

# 2
def movies_above_5_5(movies):
    return [movie for movie in movies if movie["imdb"] > 5.5]

# 3
def movies_in_category(movies, category):
    return [movie for movie in movies if movie["category"] == category]

# 4
def average_imdb_score(movies):
    if not movies:
        return 0
    total_score = sum(movie["imdb"] for movie in movies)
    return total_score / len(movies)

# 5
def average_imdb_score_by_category(movies, category):
    category_movies = movies_in_category(movies, category)
    return average_imdb_score(category_movies)

print(is_above_5_5(movies[0]))
print(movies_above_5_5(movies))
print(movies_in_category(movies, "Romance"))
print(average_imdb_score(movies))
print(average_imdb_score_by_category(movies, "Romance"))