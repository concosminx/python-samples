accounts = {
    'checking': 1000.00,
    'savings': 500.99
}

def add_balance(amount: float, name: str) -> float:
    accounts[name] += amount
    return accounts[name]


transactions = [
    (-21.12, 'checking'),
    (4.10, 'checking'),
    (-2.00, 'checking'),
    (98.15, 'savings'),
    (45.17, 'checking'),
    (-4.12, 'checking'),
    (46.12, 'checking'),
    (7.12, 'checking'),
    (91.12, 'savings'),
]

for t in transactions:
    add_balance(*t)  # add_balance(t[0], t[1]) argument unpacking

for t in transactions:
    add_balance(amount=t[0], name=t[1])  # name parameters

print(' -- second section -- ')

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<U: {self.username} P: {self.password}>'

    @classmethod
    def from_dict(cls, data):
        return cls(data['username'], data['password'])


users = [
    {'username': 'Cosmin', 'password': '1234'},
    {'username': 'Admin', 'password': 'strong_pass'},
]


# user_objects = map(User.from_dict, users)
# user_objects = [User(data['username'], data['password']) for data in users]
user_objects = [User(**data) for data in users]  # dictionary unpacking

print(list(user_objects))

