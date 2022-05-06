# argument mutability
friends_last_seen = {
    'Lili': 20,
    'Lola': 1,
    'Leo': 9
}


# mutates the value for name
def see_friend(friends, name):
    friends[name] = 0

print(id(friends_last_seen))
print(id(friends_last_seen['Lili']))
see_friend(friends_last_seen, 'Lili')

print(id(friends_last_seen['Lili']))
print(id(friends_last_seen))
print(friends_last_seen)

print(' --- second section ---- ')

age = 20


def increase_age(current_age):
    current_age = current_age + 1


print(id(age))
increase_age(age)
print(id(age)) # same id here
print(' ---- third section ---- ')

primes = [2, 3, 5]
print(id(primes))
primes += [7, 11]
print(id(primes)) # same id here
primes = [2, 3, 5] + [7, 11]
print(id(primes))  # different id here
