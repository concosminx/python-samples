accounts = {
    'checking': 1957.99,
    'savings': 3678.00
}


# the default arguments need to be at the end
def add_balance(amount: float, name: str = 'checking') -> float:
    """
    Function to update the balance of an account and return the new balance
    :param amount:
    :param name:
    :return:
    """
    accounts[name] += amount
    return accounts[name]


# add_balance(500, 'savings')
# print(accounts['savings'])

add_balance(500.00)
print(accounts)