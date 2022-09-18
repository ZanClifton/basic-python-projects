from datetime import datetime
from database import add_movie, add_user, create_table, get_movies, get_watched_movies, search_movies, watch_movie
from art import logo

menu = """What would you like to do?

Please select a number:
1) Add a new movie
2) View upcoming movies
3) View all movies
4) Add a movie to your watched list
5) View watched movies
6) Add a new user
7) Search for a movie
8) Exit

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


def prompt_add_user():
    username = input("Please enter a username for yourself: ")
    add_user(username)


def print_movie_list(header, movies):
    print(f"\n{header} MOVIES\n")
    for _id, title, release_date in movies:
        date = datetime.fromtimestamp(release_date)
        stringified_date = datetime.strftime(date, "%d-%m-%Y")
        print(f"{_id}: {title}, release date {stringified_date}")
    print("\n")


def prompt_search_movies():
    query = input("What film(s) are you looking for? ")
    movies = search_movies(query)
    if movies:
        print_movie_list("FOUND THE FOLLOWING", movies)
    else:
        print(f"\nNo matches for '{query}' found\n")


def prompt_watch_movie():
    watcher_name = input("What is your username? ")
    movie = input("What is the ID of the movie you watched? ")
    watch_movie(watcher_name=watcher_name, movie_id=movie)


def prompt_show_watched_movies():
    watcher_name = input("What is your username? ")
    print_movie_list(header=f"{watcher_name.upper()}'S WATCHED", movies=get_watched_movies(
        watcher_name=watcher_name))


while (user_input := input(menu)) != "8":
    if user_input == "1":
        prompt_add_movie()
    elif user_input == "2":
        print_movie_list("UPCOMING", get_movies(upcoming=True))
    elif user_input == "3":
        print_movie_list("ALL", get_movies())
    elif user_input == "4":
        prompt_watch_movie()
    elif user_input == "5":
        prompt_show_watched_movies()
    elif user_input == "6":
        prompt_add_user()
    elif user_input == "7":
        prompt_search_movies()
    else:
        print("Invalid input, please try again!")
