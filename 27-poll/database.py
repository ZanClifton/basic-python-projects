# Imports

from typing import List, Tuple
from psycopg2.extras import execute_values

# Types

Poll = Tuple[int, str, str]
Vote = Tuple[str, int]
PollWithOption = Tuple[int, str, str, int, str, int]
PollResults = Tuple[int, str, int, float]

# SQL Queries

# Create Tables

CREATE_POLLS = """CREATE TABLE IF NOT EXISTS polls
(id SERIAL PRIMARY KEY, title TEXT, owner_username TEXT);"""

CREATE_OPTIONS = """CREATE TABLE IF NOT EXISTS options
(id SERIAL PRIMARY KEY, option_text TEXT, poll_id INTEGER, FOREIGN KEY(poll_id) REFERENCES polls (id));"""

CREATE_VOTES = """CREATE TABLE IF NOT EXISTS votes
(username TEXT, option_id INTEGER, FOREIGN KEY(option_id) REFERENCES options (id));"""

# Fetch

SELECT_ALL_POLLS = "SELECT * FROM polls;"

SELECT_POLL_WITH_OPTIONS = """SELECT * FROM polls
JOIN options ON polls.id = options.poll_id
WHERE polls.id = %s;"""

SELECT_LATEST_POLL = """SELECT * FROM polls
JOIN options ON polls.id = options.poll.id
WHERE polls.id = (
    SELECT id FROM polls ORDER BY id DESC LIMIT 1
);"""

SELECT_RANDOM_VOTE = "SELECT * FROM votes WHERE option_id = %s ORDER BY RANDOM() LIMIT 1;"

SELECT_POLL_VOTE_PERCENTAGE = """
SELECT
    options.id,
    options.option_text,
    COUNT(votes.option_id) AS vote_count,
    COUNT(votes.option_id) / SUM(COUNT(votes.option_id)) OVER() * 100.0 AS vote_percentage
FROM options
LEFT JOIN votes ON options.id = votes.option_id
WHERE options.poll_id = %s
GROUP BY options.id;
"""

RANK_POLL_RESULTS = """
SELECT
  polls.title,
  COUNT(votes) as vote_count,
  RANK() OVER(ORDER BY COUNT(votes) DESC)
FROM polls
LEFT JOIN options ON options.poll_id = polls.id
LEFT JOIN votes ON votes.option_id = options.id
GROUP BY polls.title
ORDER BY vote_count DESC;
"""

RANK_RESULTS_BY_POLL = """
SELECT
  polls.title,
  options.option_text,
  COUNT(votes) AS vote_count,
  RANK() OVER(PARTITION BY polls.title ORDER BY COUNT(votes) DESC)
FROM polls
LEFT JOIN options ON options.poll_id = polls.id
LEFT JOIN votes ON votes.option_id = options.id
GROUP BY polls.title, options.option_text;
"""

SELECT_HIGHEST_VOTE_COUNT_ALL_POLLS = """
SELECT
    DISTINCT ON (options.poll_id) poll_id,
    options.id,
    options.option_text,
    options.poll_id,
    COUNT(votes.option_id) AS vote_count
FROM options
LEFT JOIN votes ON options.id = votes.option_id
GROUP BY options.id
ORDER BY poll_id, vote_count DESC;
"""

# Insert

INSERT_OPTION = "INSERT INTO options (option_text, poll_id) VALUES %s;"

INSERT_POLL_RETURNING_ID = "INSERT INTO polls (title, owner_username) VALUES (%s, %s) RETURNING id;"

INSERT_VOTE = "INSERT INTO votes (username, option_id) VALUES (%s, %s);"


# Functions

def create_tables(connection):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_POLLS)
            cursor.execute(CREATE_OPTIONS)
            cursor.execute(CREATE_VOTES)


def get_polls(connection) -> List[Poll]:
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(SELECT_ALL_POLLS)
            return cursor.fetchall()


def get_latest_poll(connection) -> List[PollWithOption]:
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(SELECT_LATEST_POLL)
            return cursor.fetchall()


def get_poll_details(connection, poll_id: int) -> List[PollWithOption]:
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(SELECT_POLL_WITH_OPTIONS, (poll_id,))
            return cursor.fetchall()


def get_poll_and_vote_results(connection, poll_id: int) -> List[PollResults]:
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(SELECT_POLL_VOTE_PERCENTAGE, (poll_id,))
            return cursor.fetchall()


def get_random_poll_vote(connection, option_id: int) -> Vote:
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(SELECT_RANDOM_VOTE, (option_id,))
            return cursor.fetchone()


def create_poll(connection, title: str, owner: str, options: List[str]):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(INSERT_POLL_RETURNING_ID, (title, owner))

            poll_id = cursor.fetchone()[0]
            option_values = [(option_text, poll_id) for option_text in options]

            execute_values(cursor, INSERT_OPTION, option_values)


def add_poll_vote(connection, username: str, option_id: int):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(INSERT_VOTE, (username, option_id))
