#sets
a_set = {"Robo", "Lenny"}
b_set = {"Beka"}

a_set.add("Romma")
a_set.add("Romma")
print(a_set)

a_set.remove("Robo")
print(a_set)

x = {"Rollo", "Ragnar", "Ivar"}
y = {"Ivar", "Ube"}

#in x but not in y
x_but_not_y = x.difference(y)
print(x_but_not_y)

#not in both
not_in_both = x.symmetric_difference(y)
print(not_in_both)

#intersection
x_and_y = x.intersection(y)
print(x_and_y)

#union
x_or_y = x.union(y)
print(x_or_y)

