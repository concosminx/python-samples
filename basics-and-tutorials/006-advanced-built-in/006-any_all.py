friends = [
  {
    'name': 'Alice',
    'location': 'London'
  },
  {
    'name': 'Anna',
    'location': 'Paris'
  },
  {
    'name': 'Gheorhita',
    'location': 'Bucuresti'
  },
  {
    'name': 'Jose',
    'location': 'Mexico City'
  },
]

your_location = input('Where are you right now? ')
friends_nearby = [friend for friend in friends if friend['location'] == your_location]

if any(friends_nearby):
    print('You are not alone!')


"""
Some values always evaluate to `False`:

* `0`
* `None`
* `[]`
* `()`
* `{}`
* `False`

"""