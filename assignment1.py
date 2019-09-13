"""
Replace the contents of this module docstring with your own details
Name:Matthew Howlett
Date started: 2/9/2019
GitHub URL: https://github.com/cp1404-students/2019-2-a1-MatthewHowlett
"""


def main():
    """..."""
    file = open("movies.csv", "r")
    movies = file.readlines()
    for i, movie in enumerate(movies):
        movies[i] = movie.split(",")
    print("Movies To Watch 1.0 - by Matthew Howlett")
    again = True
    while again:
        choice = input("Menu: \n L - List movies \n A - Add new movie \n W - Watch a movie \n Q - Quit").upper()
        if choice == "L":
            list_movies(movies)
        elif choice == "A":
            add_movie(movies)
        elif choice == "W":
            watch_movie(movies)
        elif choice == "Q":
            again = False
            print("Have a nice day :)")
        else:
            print("Invalid menu choice")
    file.close()


def list_movies(movies):
    watched = 0
    unwatched = 0
    for i, movie in enumerate(movies):
        if movie[3] == "w\n":
            print("{:5}{:35} - {:4} ({})".format(str(i) + ".", movie[0], movie[1], movie[2]))
            watched += 1
        else:
            print("{:3}{:2}{:35} - {:4} ({})".format(str(i) + ".", "*", movie[0], movie[1], movie[2]))
            unwatched += 1
    print("{} movies watched, {} movies still to watch".format(watched, unwatched))


def check_error(minimum, maximum, variable_to_be_checked):
    try:
        if int(variable_to_be_checked) < minimum:
            print("Number must be >=", minimum)
            return False
        elif int(variable_to_be_checked) > maximum:
            print("Number must be <=", maximum)
            return False
        else:
            return True
    except ValueError:
        print("Invalid input; enter a valid number")
        return False


def add_movie(movies):
    new_movie = []
    title = input("Title: ")
    new_movie.append(title)
    year_made = input("Year: ")
    while not check_error(0, 2019, year_made):
        year_made = input("Year: ")
    new_movie.append(year_made)
    genre = input("Category: ")
    while genre == "":
        print("Input cannot be blank")
        genre = input("Category")
    new_movie.append(genre)
    new_movie.append("u")
    movies.append(new_movie)
    print("{} ({} from {}) added to movie list".format(title, genre, year_made))


def watch_movie(movies):
    unwatched = 0
    for i, movie in enumerate(movies):
        if movie[3] == "u\n":
            unwatched += 1
    if unwatched == 0:
        print("No more movies to watch!")
        return None
    watched_movie_number = input("Enter the number of a movie to mark as watched")
    while not check_error(0, len(movies), watched_movie_number):
        watched_movie_number = input("Enter the number of a movie to mark as watched")
    if movies[int(watched_movie_number)][3] == "w\n":
        print("You have already watched", movies[int(watched_movie_number)][0])
        return None
    movies[int(watched_movie_number)][3] = "w\n"
    print(movies[int(watched_movie_number)][0], "from", movies[int(watched_movie_number)][1], "watched")


if __name__ == '__main__':
    main()
