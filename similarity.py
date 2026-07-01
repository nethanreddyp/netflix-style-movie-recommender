import csv

MOVIES_FILE = "tmdb_5000_movies.csv"


def load_movies():
    movies = []

    with open(MOVIES_FILE, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            movies.append(row)

    return movies


def calculate_similarity(selected_movie):

    movies = load_movies()

    recommendations = []

                                                                        # Get selected movie genre
    selected_genre = selected_movie["genres"]

                                                                            # Get selected movie rating
    selected_rating = float(selected_movie["vote_average"])

    for movie in movies:

                                                                            # Skip the searched movie
        if movie["title"] == selected_movie["title"]:
            continue

        score = 0

                                                                # Genre Match
        if movie["genres"] == selected_genre:
            score += 40

                                                                    # Rating Match
        try:
            rating = float(movie["vote_average"])

            if abs(rating - selected_rating) <= 1:
                score += 10

        except:
            pass

        recommendations.append((score, movie))

    recommendations.sort(reverse=True, key=lambda x: x[0])

    return recommendations[:10]