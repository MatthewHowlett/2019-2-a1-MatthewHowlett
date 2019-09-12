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


if __name__ == '__main__':
   main()
