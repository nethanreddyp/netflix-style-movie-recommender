HISTORY_FILE = "history.txt"


def save_history(movie_name):

    with open(HISTORY_FILE, "a", encoding="utf-8") as file:
        file.write(movie_name + "\n")


def view_history():

    try:

        with open(HISTORY_FILE, "r", encoding="utf-8") as file:
            history = file.readlines()

        return [movie.strip() for movie in history if movie.strip()]

    except FileNotFoundError:

        return []