import json

#how to use context managers - read
with open('005-friends-json.txt', 'r') as file:
    file_contents = json.load(file)  

print(file_contents['friends'][0])


cars = [
    {'make': 'Ford', 'model': 'Fiesta'},
    {'make': 'Ford', 'model': 'Focus'}
]

#how to use context managers - write
with open('005-cars-json.txt', 'w') as file:
    json.dump(cars, file)


my_json_string = '[{"name": "Alfa Romeo", "released": 1950}]'

incorrect_car = json.loads(my_json_string)
print(incorrect_car[0]['name'])
