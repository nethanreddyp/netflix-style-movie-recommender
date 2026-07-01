import pandas as pd

# Load datasets
movies = pd.read_csv("tmdb_5000_movies.csv")
credits = pd.read_csv("tmdb_5000_credits.csv")

# Merge datasets
movies = movies.merge(credits, on="title")


def search_movie(query):

    query = query.lower()

    # Search in movie title
    title_results = movies[
        movies["title"].str.lower().str.contains(query, na=False)
    ]

    # Search in overview (keywords/story)
    overview_results = movies[
        movies["overview"].str.lower().str.contains(query, na=False)
    ]

    # Search in cast
    cast_results = movies[
        movies["cast"].str.lower().str.contains(query, na=False)
    ]

    # Search in crew (director, producer, etc.)
    crew_results = movies[
        movies["crew"].str.lower().str.contains(query, na=False)
    ]

    # Combine all results
    results = pd.concat([
        title_results,
        overview_results,
        cast_results,
        crew_results
    ])

    # Remove duplicates
    results = results.drop_duplicates(subset="title")

    # Return only title column
    return results[["title"]].head(10)