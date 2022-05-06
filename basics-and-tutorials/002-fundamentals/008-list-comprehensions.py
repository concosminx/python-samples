numbers = [0,1,2,3,4]
doubled_numbers = []

#for number in numbers:
#    doubled_numbers.append(number*2)
#
#print(doubled_numbers)

doubled_numbers=[number*2 for number in numbers]
print(doubled_numbers)

a_new_list = [number*2 for number in range(6)]
print(a_new_list)

ages = [22,33,11,23]
age_strings = [f"My age is {age}" for age in ages]
print(age_strings)


names=["Cosmin", "Raluca", "Vlad"]
lower = [name.lower() for name in names]
print(lower)

#with ifs
ages = [22, 35, 27, 21, 20]
odds = [n for n in ages if n % 2 == 1]
print(odds)


friends = ["Rolf", "ruth", "charlie", "Jen"]
guests = ["jose", "Bob", "Rolf", "Charlie", "michael"]

friends_lower = [f.lower() for f in friends]

present_friends = [
    name.capitalize() for name in guests if name.lower() in friends_lower
]
print(present_friends)

friends = ["Rolf", "ruth", "charlie", "Jen"]
guests = ["jose", "Bob", "Rolf", "Charlie", "michael"]

present_friends = [
    name.capitalize() for name in guests if name.lower() in [f.lower() for f in friends]
]
print(present_friends)
