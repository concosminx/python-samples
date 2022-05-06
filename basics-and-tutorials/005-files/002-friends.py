# ask the user for a list of 3 friends
friends = input('Enter three friend names, separated by commas: ').split(',')

people = open('002-people.txt', 'r')
people_nearby = [line.strip() for line in people.readlines()]

people.close()

friends_set = set(friends)
people_nearby_set = set(people_nearby)

friends_nearby_set = friends_set.intersection(people_nearby_set)

nearby_friends_file = open('002-nearby_friends.txt', 'w')

for friend in friends_nearby_set:
    print(f'{friend} is nearby! Meet up with them.')
    nearby_friends_file.write(f'{friend}\n')

nearby_friends_file.close()