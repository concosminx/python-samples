lottery_numbers = {13, 21, 22, 5, 8}

players = [
    {
        'name': 'Ragnar',
        'numbers': {1, 3, 8, 22, 21}
    },
    {
        'name': 'Rollo',
        'numbers': {4, 9, 10, 12, 15}
    }
]
name = players[0]['name']
numbers = players[0]['numbers'].intersection(lottery_numbers)
print('Player {name} got {amount} numbers right.'.format(name=name, amount=len(numbers)))
name = players[1]['name']
numbers = players[1]['numbers'].intersection(lottery_numbers)
print('Player {name} got {amount} numbers right.'.format(name=name, amount=len(numbers)))