import datetime
import sqlite3

CREATE_MOVIES_TABLE = """CREATE TABLE IF NOT EXISTS movies (
    id INTEGER PRIMARY KEY,
    title TEXT,
    release_timestamp REAL
);
"""

CREATE_USERS_TABLE = """CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY
);
"""

CREATE_WATCHED_TABLE = """CREATE TABLE IF NOT EXISTS watched (
    user_username TEXT,
    movie_id INTEGER,
    FOREIGN KEY(user_username) REFERENCES users(username),
    FOREIGN KEY(movie_id) REFERENCES movies(id)
);
"""

INSERT_MOVIE = "INSERT INTO movies(title, release_timestamp, watched) VALUES (?, ?, 0);"
INSERT_USER = "INSERT INTO users(username) VALUES (?);"
SELECT_ALL_MOVIES = "SELECT * FROM movies;"
SELECT_UPCOMING_MOVIES = "SELECT * FROM movies WHERE release_timestamp > ?;"
SELECT_WATCHED_MOVIES = "SELECT * FROM watched WHERE user_username = ?;"
INSERT_WATCHED_MOVIE = "INSERT INTO watched(watcher_name, title) VALUES (?, ?);"
DELETE_MOVIE = "DELETE FROM movies WHERE title = ?;"

connection = sqlite3.connect("data.db")
connection.row_factory = sqlite3.Row


def create_table():
    with connection:
        connection.execute(CREATE_MOVIES_TABLE)
        connection.execute(CREATE_USERS_TABLE)
        connection.execute(CREATE_WATCHED_TABLE)


def add_movie(title, release_timestamp):
    with connection:
        connection.execute(INSERT_MOVIE, (title, release_timestamp))


def get_movies(upcoming=False):
    with connection:
        if upcoming:
            today_timestamp = datetime.datetime.today().timestamp()
            cursor = connection.execute(SELECT_UPCOMING_MOVIES, (today_timestamp,))
            return cursor.fetchall()
        cursor = connection.execute(SELECT_ALL_MOVIES)
        return cursor.fetchall()


def get_watched_movies(username):
    with connection:
        cursor = connection.execute(SELECT_WATCHED_MOVIES, (username,))
        return cursor.fetchall()


def watch_movie(username, movie_id):
    with connection:
        connection.execute(
            INSERT_WATCHED_MOVIE,
            (
                username,
                movie_id,
            ),
        )


def delete_movie(title):
    with connection:
        connection.execute(DELETE_MOVIE, (title,))


def add_user(username):
    with connection:
        connection.execute(
            INSERT_USER,
            (username,),
        )
