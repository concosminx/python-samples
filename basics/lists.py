#lists

friends = ["Ragnar", "Ube", "Rollo", "Bjorn"]
print(friends[1])

#append
friends.append("Ivar")
print(friends)
friends.remove("Ube")
print(friends)

others = [
    ["Rolf", 24],
    ["Rollo", 45],
    ["Remy", 13],
]
print(others[0][1])
others.remove(["Rolf", 24])
print(others)

grades = [7, 8, 10, 5]

total = sum(grades)
length = len(grades)

average = total / length
print(average)

names = ["Lolec", "Bolec", "Mira"]
comma_sep = ", ".join(names)
print(comma_sep)