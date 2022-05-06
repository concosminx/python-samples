friends_last_seen = {
    'Rolf': 31,
    'Jen': 1,
    'Anne': 7
}

print(id(friends_last_seen))

friends_last_seen = {
    'Rolf': 31,
    'Jen': 1,
    'Anne': 7
}

print(id(friends_last_seen))

print('------ first two with different ids ---------')

friends_last_seen = {
    'Rolf': 31,
    'Jen': 1,
    'Anne': 7
}

print(id(friends_last_seen))
friends_last_seen['Anne'] = 20
print(id(friends_last_seen))
print('----- same object with modified content ------')


"""
Immutable things in Python:

* integers
* floats
* strings
* tuples
"""

age = 20
print(id(age))

age = 30
print(id(age))

print('---- ids for numbers ------')


greeting = 'hello'
print(id(greeting))

greeting = 'byebye'
print(id(greeting))

greeting = greeting + 'a'
print(id(greeting))

print('---- ids for strings ------')

my_tuple = (3, 5, 10)
print(id(my_tuple))

my_tuple = (3, 5)
print(id(my_tuple))

print('---- ids for tuples ------')

friends = ['Rolf', 'Jose']
print(id(friends))

friends.append('Jen')
print(id(friends))

print('---- lists are mutable, as expected :) ------')