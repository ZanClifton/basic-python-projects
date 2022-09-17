from datetime import datetime
from database import add_movie, create_table, get_movies, get_watched_movies, watch_movie
from art import logo

menu = """What would you like to do?

Please select a number:
1) Add a new movie
2) View upcoming movies
3) View all movies
4) Update a movie to watched
5) View watched movies
6) Exit

Your selection: """

welcome = "Welcome to the watchlist app!"

print(logo)
print(welcome)
create_table()


def prompt_add_movie():
    movie = input("What's the movie called? ")
    release_date = input("And the release date? (dd-mm-YYYY) ")
    parsed_date = (datetime.strptime(release_date, "%d-%m-%Y"))
    timestamp = parsed_date.timestamp()

    add_movie(title=movie, release_timestamp=timestamp)


def print_movie_list(header, movies):
    print(f"\n{header} MOVIES\n")
    for movie in movies:
        date = datetime.fromtimestamp(movie[1])
        stringified_date = datetime.strftime(date, "%d-%m-%Y")
        print(f"{movie[0]}, release date {stringified_date}")
    print("\n")


def print_watched_movie_list(watcher_name, movies):
    print(f"{watcher_name.upper()}'S WATCHED MOVIES")
    for movie in movies:
        print(f"{movie[1]}")
    print("\n")


def prompt_watch_movie():
    watcher_name = input("What is your username? ")
    movie = input("Which movie did you watch? ")
    watch_movie(watcher_name=watcher_name, title=movie)


while (user_input := input(menu)) != "6":
    if user_input == "1":
        prompt_add_movie()
    elif user_input == "2":
        print_movie_list("UPCOMING", get_movies(upcoming=True))
    elif user_input == "3":
        print_movie_list("ALL", get_movies())
    elif user_input == "4":
        prompt_watch_movie()
    elif user_input == "5":
        watcher_name = input("What is your username? ")
        print_watched_movie_list(watcher_name=watcher_name, movies=get_watched_movies(
            watcher_name=watcher_name))
    else:
        print("Invalid input, please try again!")
