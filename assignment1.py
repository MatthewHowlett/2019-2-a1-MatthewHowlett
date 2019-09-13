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
        if movie.split(",")[3] == "w\n":
            print("{:5}{:35} - {:4} ({})".format(str(i) + ".", movie.split(",")[0], movie.split(",")[1], movie.split(",")[2]))
            watched += 1
        else:
            print("{:3}{:2}{:35} - {:4} ({})".format(str(i) + ".", "*", movie.split(",")[0], movie.split(",")[1], movie.split(",")[2]))
            unwatched += 1
    print("{} movies watched, {} movies still to watch".format(watched, unwatched))


def check_error(minimum, maximum, variable_to_be_checked):
    try:
        if int(variable_to_be_checked) < minimum or int(variable_to_be_checked) > maximum:
            return False
        else:
            return True
    except ValueError:
        print("Input must be an integer")
        return False


def add_movie(movies):
    title = input("Enter movie title: ")
    year_made = input("Enter year made: ")
    while not check_error(0, 2019, year_made):
        print("Year made must be between 0 and 2019")
        year_made = input("Enter year made: ")
    genre = input("Enter genre: ")
    new_movie = title + "," + year_made + "," + genre + ",u"
    movies.append(new_movie)


if __name__ == '__main__':
    main()
