def greet():
    print("hello")


def before_and_after(func):
    print("Before...")
    func()
    print("After...")


before_and_after(lambda: 65)
before_and_after(greet)

movies = [
    {'name': 'Matrix', 'director' : "Wachowski"},
    {'name': '1917', 'director' : "Mendes"},
    {'name': 'Klaus', 'director' : "Pablos"},
]


def find_movie(expected, finder):
    for m in movies:
        if finder(m) == expected:
            return m


find_by = input("What property are we searching for? ")
looking_for = input("What are you looking for? ")
found_movie = find_movie(looking_for, lambda movie: movie[find_by])
print(found_movie or 'No movies found')