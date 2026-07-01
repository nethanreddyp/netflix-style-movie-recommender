from search import search_movie               #search
from recommendation_engine import recommend   #recommendation
from genre import browse_genre                #Genre
from top_rated import top_rated_movies        #top rated
from year import search_by_year               #search by year
from random_movie import random_movie         #random suggestion
from history import save_history, view_history    #history

while True:

    print("\n" + "=" * 60)
    print("           MOVIE RECOMMENDATION SYSTEM")
    print("=" * 60)
    print("1. Search Movie")
    print("2. Browse by Genre")
    print("3. Top Rated Movies")
    print("4. Search by Year")
    print("5. Random Movie Recommendation")
    print("6. History")
    print("7. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":        #Search movie

        query = input("\nSearch Movie: ")

        results = search_movie(query)

        if results.empty:
            print("\nMovie not found.")
            continue

        print("\nSearch Results\n")

        titles = results["title"].tolist()

        for i, movie in enumerate(titles, start=1):
            print(f"{i}. {movie}")

        try:
            movie_choice = int(input("\nChoose Movie Number: "))

            if movie_choice < 1 or movie_choice > len(titles):
                print("\nInvalid Choice")
                continue

        except ValueError:
            print("\nPlease enter a valid number.")
            continue

        selected_movie = titles[movie_choice - 1]

        save_history(selected_movie)

        recommendations = recommend(selected_movie)

        print("\n" + "=" * 60)
        print(f"Recommendations for: {selected_movie}")
        print("=" * 60)

        for i, movie in enumerate(recommendations, start=1):
            print(f"{i}. {movie}")


    elif choice == "2":                #browse by genre

        genre = input("\nEnter Genre: ")

        genre_movies = browse_genre(genre)

        if len(genre_movies) == 0:
            print("\nNo movies found.")

        else:
            print("\nTop Movies\n")

            for i, movie in enumerate(genre_movies, start=1):
                print(f"{i}. {movie}")
                      
    elif choice == "3":             #top rated movies

        print("\n" + "=" * 60)
        print("               TOP RATED MOVIES")
        print("=" * 60)

        movies = top_rated_movies()

        for i, (_, row) in enumerate(movies.iterrows(), start=1):
            print(f"{i}. {row['title']} ({row['vote_average']})")

    elif choice == "4":              #search by year

        year = input("\nEnter Release Year: ")

        movies = search_by_year(year)

        if movies.empty:
            print("\nNo movies found.")

        else:
            print(f"\nMovies Released in {year}\n")

            for i, (_, row) in enumerate(movies.iterrows(), start=1):
                print(f"{i}. {row['title']}")

    elif choice == "5":     #random movie recommendation

        movie = random_movie()

        print("\nToday's Recommended Movie")
        print("-" * 30)
        print(movie)

        save_history(movie)

        recommendations = recommend(movie)

        print("\nYou May Also Like\n")

        for i, m in enumerate(recommendations, start=1):
            print(f"{i}. {m}")

    elif choice == "6":                                    #view search history

        history = view_history()

        print("\n" + "=" * 60)
        print("                 SEARCH HISTORY")
        print("=" * 60)

        if len(history) == 0:
            print("No search history found.")

        else:
            for i, movie in enumerate(history, start=1):
                print(f"{i}. {movie}")


    elif choice == "7":               #exit

        print("\nThank you for using the Movie Recommendation System!")
        break

    else:                      #invalid choice

        print("\nInvalid Choice. Please try again.")