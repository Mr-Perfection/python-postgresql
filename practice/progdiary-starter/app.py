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
    watch_movie(input("Movie title: "))


def print_watched_movies_list():
    print_movies_list("Watched", get_watched_movies())


def print_movies_list(heading, movies):
    print(f"-- {heading} Movies --")
    for movie in movies:
        movie_date = datetime.datetime.fromtimestamp(movie["release_timestamp"])
        print(f"{movie['title']} {movie_date.strftime('%b %d %Y')}")
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
        print_watched_movies_list()
    else:
        print("Invalid input, please try again!")
