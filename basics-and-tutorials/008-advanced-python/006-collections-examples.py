# how to use Counter
print('---counter---')
from collections import Counter

device_temperatures = [13.5, 14.0, 14.0, 14.5, 14.5, 14.5, 15.0, 16.0]

temperature_counter = Counter(device_temperatures)
print(temperature_counter[14.0])  # 2

## defaultdict
print('---defaultdict---')
alma_maters = {}
coworkers = [('Rolf', 'MIT'), ('Jen', 'Oxford'), ('Rolf', 'Cambridge'), ('Charlie', 'Manchester')] 

# for coworker in coworkers:
#     if not coworker[0] in alma_maters:
#         alma_maters[coworker[0]] = []
#     alma_maters[coworker[0]].append(coworker[1])

from collections import defaultdict

coworker_alma_maters = defaultdict(list)  # list is a function, returns []
for coworker, place in coworkers:
    coworker_alma_maters[coworker].append(place)

print(coworker_alma_maters['Rolf'])
print(coworker_alma_maters['Anne'])  # []

from collections import defaultdict

my_company = 'SupaDupaFly'

coworkers = ['Jen', 'Li', 'Charlie', 'Rhys']
other_coworkers = [('Rolf', 'Apple Inc.'), ('Anna', 'Google')]

coworker_companies = defaultdict(lambda: my_company)

for person, company in other_coworkers:
    coworker_companies[person] = company

print(coworker_companies['Jen'])  # SupaDupaFly
print(coworker_companies['Rolf'])  # Apple Inc.

from collections import defaultdict

int_dict = defaultdict(int)

int_dict['first'] += 1
print(int_dict['first'])  # 1

int_dict.default_factory = list
int_dict['second'].append('Rolf')
print(int_dict['second'])  # ['Rolf']

int_dict.default_factory = None  # this is back to being a "normal dictionary"

## OrderedDict
print('---OrderedDict---')
from collections import OrderedDict

o = OrderedDict()
o['Rolf'] = 6
o['Jose'] = 10
o['Jen'] = 3

print(o)  # insert is preserving order

o.move_to_end('Rolf')
o.move_to_end('Jose', last=False)

print(o)

o.popitem()

print(o)


## namedtuple
print('---namedtuple---')
account = ('checking', 1850.90)

print(account[0])  # name
print(account[1])  # balance

from collections import namedtuple

Account = namedtuple('Account', ['name', 'balance'])

account = Account('checking', 1850.90)
print(account.name)
print(account.balance)

# print the account itself with a nice __repr__
print(account)


name, balance = account  # tuple destructuring

Account('checking', balance=1850.90)  # use positional or named arguments

Account._make(('checking', 1850.90))

accounts = [
    ('checking', 1850.90),
    ('savings', 3658.00),
    ('credit', -450.00)
]

account_tuples = map(Account._make, accounts)

account._asdict()  # an OrderedDict representing the tuple


## Deque
print('---Deque---')
from collections import deque

friends = deque(('Rolf', 'Charlie', 'Jen', 'Anna'))
friends.append('Jose')
friends.appendleft('Anthony')

print(friends)

friends.pop()
print(friends)

friends.popleft()
print(friends)