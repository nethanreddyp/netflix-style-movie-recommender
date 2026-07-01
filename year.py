import pandas as pd

movies = pd.read_csv("tmdb_5000_movies.csv")


def search_by_year(year):

    result = movies[movies["release_date"].str.startswith(str(year), na=False)]

    return result[["title"]].head(20)