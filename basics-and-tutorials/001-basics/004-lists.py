#lists
friends = ["Ragnar", "Ube", "Rollo", "Bjorn"]
print('friends[1] is: ',friends[1])

#append
friends.append("Ivar")
print('friends after appending Ivar: ', friends)
friends.remove("Ube")
print('friends after removind Ube: ',friends)

#multi dimensional
others = [
    ["Rolf", 24],
    ["Rollo", 45],
    ["Remy", 13],
]
print('others[0][1]: ', others[0][1])
others.remove(["Rolf", 24])
print('others without Rolf', others)

grades = [7, 8, 10, 5]

#predefined functions
total = sum(grades)
length = len(grades)

average = total / length
print('average: ', average)
names = ["Lolec", "Bolec", "Mira"]
comma_sep = ", ".join(names)
print('comma_sep: ', comma_sep)