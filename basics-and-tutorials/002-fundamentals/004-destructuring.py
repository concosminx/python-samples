#destructuring

currencies = 0.8, 1.2
usd, eur = currencies

print(usd)
print(eur)

#destructuring in for loop
friends = [("Joe", 31),("Jane", 23),("Kim", 26),("Ron", 26)]

for name, age in friends:
    print(name, age)