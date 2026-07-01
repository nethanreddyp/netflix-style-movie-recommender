import pandas as pd
import random

movies = pd.read_csv("tmdb_5000_movies.csv")


def random_movie():

    movie = movies.sample(1)

    return movie.iloc[0]["title"]