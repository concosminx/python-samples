import json

#read the file and transform data in json format (dictionary)
file = open('005-friends-json.txt', 'r')
file_contents = json.load(file)  
file.close()

print(file_contents['friends'][0])


cars = [
    {'make': 'Ford', 'model': 'Fiesta'},
    {'make': 'Ford', 'model': 'Focus'}
]

file = open('005-cars-json.txt', 'w')
json.dump(cars, file)
file.close()

my_json_string = '[{"name": "Alfa Romeo", "released": 1950}]'

incorrect_car = json.loads(my_json_string)
print(incorrect_car[0]['name'])
