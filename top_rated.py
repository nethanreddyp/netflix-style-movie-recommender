import pandas as pd

movies = pd.read_csv("tmdb_5000_movies.csv")


def top_rated_movies():

    top_movies = movies.sort_values(
        by="vote_average",
        ascending=False
    )

    return top_movies[["title", "vote_average"]].head(10)
