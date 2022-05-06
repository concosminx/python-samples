# mutable default arguments - bad idea!

def create_account(name: str, holder: str, account_holders: list = []):
    print(id(account_holders))
    account_holders.append(holder)

    return {
        'name' : name,
        'main_account_holder': holder,
        'account_holders': account_holders
    }


a1 = create_account('checking', 'Rolf')
print(a1)

a2 = create_account('savings', 'Jen')
print(a2)


# fixed
def create_account_fixed(name: str, holder: str, account_holders=None):
    if not account_holders:
        account_holders = []

    return {
        'name' : name,
        'main_account_holder': holder,
        'account_holders': account_holders
    }