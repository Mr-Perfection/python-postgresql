import datetime
import sqlite3

CREATE_MOVIES_TABLE = """CREATE TABLE IF NOT EXISTS movies (
    title TEXT,
    release_timestamp REAL,
    watched INTEGER
);
"""

CREATE_WATCHED_MOVIES_TABLE = """CREATE TABLE IF NOT EXISTS watched (
    watcher_name TEXT,
    title TEXT
);
"""

INSERT_MOVIE = "INSERT INTO movies(title, release_timestamp, watched) VALUES (?, ?, 0);"
SELECT_ALL_MOVIES = "SELECT * FROM movies;"
SELECT_UPCOMING_MOVIES = "SELECT * FROM movies WHERE release_timestamp > ?;"
SELECT_WATCHED_MOVIES = "SELECT * FROM watched WHERE watcher_name = ?;"
INSERT_WATCHED_MOVIE = "INSERT INTO watched(watcher_name, title) VALUES (?, ?);"
DELETE_MOVIE = "DELETE FROM movies WHERE title = ?;"

connection = sqlite3.connect("data.db")
connection.row_factory = sqlite3.Row


def create_table():
    with connection:
        connection.execute(CREATE_MOVIES_TABLE)
        connection.execute(CREATE_WATCHED_MOVIES_TABLE)


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


def watch_movie(username, title):
    with connection:
        connection.execute(DELETE_MOVIE, (title,))
        connection.execute(
            INSERT_WATCHED_MOVIE,
            (
                username,
                title,
            ),
        )


def delete_movie(title):
    with connection:
        connection.execute(DELETE_MOVIE, (title,))
