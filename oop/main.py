#a class for a movie
class Movie:
    def __init__(self, name, year):
        self.name = name
        self.year = year

    def print_movie(self):
        print('[[{}]] from {}'.format(self.name, self.year))



m1 = Movie('The Amazing Spiderman', 2005)

m1.print_movie()
Movie.print_movie(m1) #same result here

#display the class
movies = ['Finding Nemo', 'Batman']
print(movies.__class__)
print('yes'.__class__)


class Brand:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, i):
        return self.cars[i]

    def __repr__(self): #use this for code oriented description
        return f'<Brand {self.cars}>'

    def __str__(self): #use this for user oriented description
        return f'Brand with {len(self)} models'


dacia = Brand()
dacia.cars.append('Logan')
dacia.cars.append('Duster')

print(len(dacia))
print(dacia[0])
print(dacia)

for model in dacia:
    print(model)