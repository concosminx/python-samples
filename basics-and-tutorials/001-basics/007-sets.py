#sets
a_set = {"Robo", "Lenny"}
b_set = {"Beka"}

a_set.add("Romma")
a_set.add("Romma")
print('first set: ', a_set)

a_set.remove("Robo")
print('first set after removing "Robo": ', a_set)

x = {"Rollo", "Ragnar", "Ivar"}
y = {"Ivar", "Ube"}

#in x but not in y
x_but_not_y = x.difference(y)
print('diference: ', x_but_not_y)

#not in both
not_in_both = x.symmetric_difference(y)
print('symmetric difference: ',not_in_both)

#intersection
x_and_y = x.intersection(y)
print('intersection: ', x_and_y)

#union
x_or_y = x.union(y)
print('union: ', x_or_y)

