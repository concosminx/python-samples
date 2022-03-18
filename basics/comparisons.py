#booleans
thruty = True
falsy = False

age = 18
is_adult = age >= 18
print(is_adult)

print(age < 18)
print(age == 18)

age = 35#int(input("Enter your age: "))
can_drink = age > 17 and age < 60
print(f"You cand drink {can_drink}.")

usually_not_drink = age < 18 or age >= 60
print(f"At {age}, you are usually not drinking: {usually_not_drink}")

print(bool(0))
print(bool(""))
print(bool(34))

name = ""
surname = "John"
greeting = name or f"Mr. {surname}"
print(greeting)

print(not True)