CREATE_MOVIES_TABLE = """CREATE TABLE IF NOT EXIST movies VALUES(
    title TEXT,
    release_timestamp REAL,
    watched: INTEGER
);
"""

INSERT_MOVIE = "INSERT INTO movies(title, release_timestamp, watched) VALUES(?,?,0);"
SELECT_ALL_MOVIES = "SELECT * FROM movies;"
SELECT_UPCOMING_MOVIES = "SELECT * FROM movies WHERE release_timestamp > ?;"
SELECT_WATCHED_MOVIES = "SELECT * FROM movies WHERE watched = 1;"
