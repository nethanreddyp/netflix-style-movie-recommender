import pandas as pd
import ast
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from ranking import rank_movies

# Load Dataset

movies = pd.read_csv("tmdb_5000_movies.csv")
credits = pd.read_csv("tmdb_5000_credits.csv")

movies = movies.merge(credits, on="title")

# Helper Functions

def convert(obj):
    L = []

    for i in ast.literal_eval(obj):
        L.append(i["name"])

    return L


def fetch_director(obj):

    for i in ast.literal_eval(obj):

        if i["job"] == "Director":

            return i["name"]

    return ""

# Data Cleaning

movies = movies[
    [
        "movie_id",
        "title",
        "overview",
        "genres",
        "keywords",
        "cast",
        "crew",
    ]
]

movies.dropna(inplace=True)

movies["genres"] = movies["genres"].apply(convert)
movies["keywords"] = movies["keywords"].apply(convert)
movies["cast"] = movies["cast"].apply(convert)
movies["crew"] = movies["crew"].apply(fetch_director)

movies["cast"] = movies["cast"].apply(lambda x: x[:3])

movies["overview"] = movies["overview"].apply(lambda x: x.split())

movies["genres"] = movies["genres"].apply(
    lambda x: [i.replace(" ", "") for i in x]
)

movies["keywords"] = movies["keywords"].apply(
    lambda x: [i.replace(" ", "") for i in x]
)

movies["cast"] = movies["cast"].apply(
    lambda x: [i.replace(" ", "") for i in x]
)

movies["crew"] = movies["crew"].apply(
    lambda x: x.replace(" ", "")
)

movies["tags"] = (
    movies["overview"]
    + movies["genres"]
    + movies["keywords"]
    + movies["cast"]
    + movies["crew"].apply(lambda x: [x])
)

movies = movies[["movie_id", "title", "tags"]]

movies["tags"] = movies["tags"].apply(lambda x: " ".join(x))

movies["tags"] = movies["tags"].apply(lambda x: x.lower())

# TF-IDF

vectorizer = TfidfVectorizer(stop_words="english")

vectors = vectorizer.fit_transform(movies["tags"])

similarity = cosine_similarity(vectors)

# Recommendation Function

def recommend(movie_name):

    movie_name = movie_name.lower()

    movie_index = None

    for index, row in movies.iterrows():

        if row["title"].lower() == movie_name:

            movie_index = index
            break

    if movie_index is None:
        return None

    distances = list(enumerate(similarity[movie_index]))

    distances = rank_movies(distances)

    recommendations = []

    for movie in distances[1:11]:

        recommendations.append(
            movies.iloc[movie[0]].title
        )

    return recommendations