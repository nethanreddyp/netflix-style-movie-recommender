def rank_movies(similarity_scores):
    """
    Sort movies based on similarity score.
    """

    ranked_movies = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    return ranked_movies