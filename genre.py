import pandas as pd
import ast

movies = pd.read_csv("tmdb_5000_movies.csv")


def convert(obj):
    genres = []

    try:
        data = ast.literal_eval(obj)

        for item in data:
            genres.append(item["name"])

    except:
        pass

    return genres


movies["genres"] = movies["genres"].apply(convert)


def browse_genre(genre):

    genre = genre.lower()

    result = []

    for _, movie in movies.iterrows():

        genres = [g.lower() for g in movie["genres"]]

        if genre in genres:

            result.append(movie["title"])

    return result[:20]