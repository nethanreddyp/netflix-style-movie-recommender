def display_recommendations(movie_name, recommendations):

    print("\n")
    print("=" * 50)
    print("MOVIE RECOMMENDATION SYSTEM")
    print("=" * 50)

    print(f"\nSelected Movie : {movie_name}")

    print("\nYou May Also Like\n")

    for i, movie in enumerate(recommendations, start=1):

        print(f"{i}. {movie}")

    print("\n" + "=" * 50)