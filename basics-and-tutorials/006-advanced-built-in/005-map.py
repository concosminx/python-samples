friends = ['Rolf', 'Charlie', 'Anna']
friends_lower = map(lambda x: x.lower(), friends)

print('----section 1----')
print(friends_lower)
print(list(friends_lower))


print('----section 2----')
friends_lower = [friend.lower() for friend in friends]
print(friends_lower)
friends_lower = (friend.lower() for friend in friends)
print(friends_lower)

print('----section 3----')
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def from_dict(cls, data):
        return cls(data['username'], data['password'])

    def __repr__(self) -> str:
        return '<user: {}, pass: {}>'.format(self.username, self.password)


users = [
    { 'username': 'rolf', 'password': '123' },
    { 'username': 'tecladoisawesome', 'password': 'youaretoo' }
]

user_objects = map(User.from_dict, users)
print(user_objects)

user_objects = [User.from_dict(u) for u in users]
print(user_objects)