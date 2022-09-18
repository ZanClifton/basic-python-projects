import datetime
import sqlite3

CREATE_MOVIES_TABLE = """CREATE TABLE IF NOT EXISTS movies (
    id INTEGER PRIMARY KEY,
    title TEXT, 
    release_timestamp REAL
);"""

CREATE_USERS_TABLE = """CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY
);"""

CREATE_WATCHLIST_TABLE = """CREATE TABLE IF NOT EXISTS watched (
    users_username TEXT,
    movies_id TEXT,
    FOREIGN KEY(users_username) REFERENCES users(username),
    FOREIGN KEY(movies_id) REFERENCES movies(id)
);"""

INSERT_MOVIES = "INSERT INTO movies (title, release_timestamp) VALUES (?, ?);"

INSERT_USER = "INSERT INTO users (username) VALUES (?);"

DELETE_MOVIE = "DELETE FROM movies WHERE title = ?;"

SELECT_ALL_MOVIES = "SELECT * FROM movies ORDER BY release_timestamp;"

SELECT_UPCOMING_MOVIES = "SELECT * FROM movies WHERE release_timestamp > ? ORDER BY release_timestamp;"

SELECT_WATCHED_MOVIES = """SELECT movies.*
FROM movies
JOIN watched ON movies.id = watched.movies_id
JOIN users ON users.username = watched.users_username
WHERE users.username = ?;"""

INSERT_WATCHED_MOVIE = "INSERT INTO watched (users_username, movies_id) VALUES (?, ?);"

SEARCH_MOVIES = "SELECT * FROM movies WHERE title LIKE ?;"


connection = sqlite3.connect("data.db")


def create_table():
    with connection:
        connection.execute(CREATE_MOVIES_TABLE)
        connection.execute(CREATE_USERS_TABLE)
        connection.execute(CREATE_WATCHLIST_TABLE)


def add_movie(title, release_timestamp):
    with connection:
        connection.execute(INSERT_MOVIES, (title, release_timestamp))


def add_user(username):
    with connection:
        connection.execute(INSERT_USER, (username,))


def delete_movie(title):
    with connection:
        connection.execute(DELETE_MOVIE, (title,))


def get_movies(upcoming=False):
    with connection:
        cursor = connection.cursor()
        if upcoming:
            today_timestamp = datetime.datetime.today().timestamp()
            cursor.execute(SELECT_UPCOMING_MOVIES, (today_timestamp, ))
        else:
            cursor.execute(SELECT_ALL_MOVIES)
        return cursor.fetchall()


def search_movies(query):
    with connection:
        cursor = connection.cursor()
        cursor.execute(SEARCH_MOVIES, (f"%{query}%",))
        return cursor.fetchall()


def watch_movie(watcher_name, movie_id):
    with connection:
        connection.execute(INSERT_WATCHED_MOVIE, (watcher_name, movie_id))


def get_watched_movies(watcher_name):
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_WATCHED_MOVIES, (watcher_name,))
        return cursor.fetchall()
