from database import (
    add_movie,
    create_table,
    get_movies,
    watch_movie,
    get_watched_movies,
)
import datetime

menu = """Please select one of the following options:
1) Add new movie.
2) View upcoming movies.
3) View all movies
4) Watch a movie
5) View watched movies.
6) Exit.

Your selection: """
welcome = "Welcome to the watchlist app!"


print(welcome)
create_table()


def prompt_add_movie():
    title = input("Movie title: ")
    release_date = input("Release Date (dd-mm-YYYY): ")
    timestamp = datetime.datetime.strptime(release_date, "%d-%m-%Y").timestamp()
    add_movie(title, timestamp)


def prompt_watch_movie():
    watch_movie(input("Username: "), input("Movie title: "))


def _convert_movie_attribute_to_readable_form(val, key):
    # TODO(me): convert all the keys to enums
    if key == "release_timestamp":
        return datetime.datetime.fromtimestamp(val).strftime("%b %d %Y")
    else:
        return val


def _print_movies_helper(movies, keys):
    for movie in movies:
        print(movie)
        values = [_convert_movie_attribute_to_readable_form(movie[k], k) for k in keys]
        print(" ".join(values))


def print_watched_movies_list(username):
    print_movies(f"{username}'s Watched", get_watched_movies(username), ("title",))


def print_movies_list(heading, movies):
    print_movies(heading, movies, ("title", "release_timestamp"))


def print_movies(heading, movies, keys):
    print(f"-- {heading} Movies --")
    _print_movies_helper(movies, keys)
    print("--- \n")


while (user_input := input(menu)) != "6":
    if user_input == "1":
        prompt_add_movie()
    elif user_input == "2":
        print_movies_list("Upcoming", get_movies(True))
    elif user_input == "3":
        print_movies_list("All", get_movies())
    elif user_input == "4":
        prompt_watch_movie()
    elif user_input == "5":
        print_watched_movies_list(input("Username: "))
    else:
        print("Invalid input, please try again!")
