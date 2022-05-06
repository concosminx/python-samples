#movie database application (using comand line)

MENU_PROMPT = "\nEnter 'a' to add a new movie, 'l' to list the movies, 'f' to find a movie by title, or 'q' to quit: "
movies = []

def add_movie():
    title = input("Movie title: ")
    year = input("Release year: ")

    movies.append({
        'title': title,
        'year': year
    })


def show_movies():
    for movie in movies:
        print_movie(movie)


def print_movie(movie):
    print(f"Title: {movie['title']}")
    print(f"Release year: {movie['year']}")


def find_movie():
    search_title = input("Enter movie title you're looking for: ")

    for movie in movies:
        if movie["title"] == search_title:
            print_movie(movie)


available_options = {
    "a": add_movie,
    "l": show_movies,
    "f": find_movie
}


def menu():
    option = input(MENU_PROMPT)
    while option != 'q':
        if option in available_options:
            selected_function = available_options[option]
            selected_function()
        else:
            print('Not a command. Try again.')

        option = input(MENU_PROMPT)


menu()
