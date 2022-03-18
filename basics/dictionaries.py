#dictionaries

ages = {"Rollo" : 26, "Ragnar" : 25, "Ube" : 31}
print(ages["Rollo"])

ages['Joe'] = 13
print(ages)

friends = (
    {"name" : "Rolo Bolo", "age" : 23},
    {"name" : "Rolo Selo", "age" : 21},
    {"name" : "Rolo Pelo", "age" : 26},
)

print(friends[2]["name"])

something = [("R", 23), ("W", 14), ("L", 3)]
a_new_dict = dict(something)
print(a_new_dict)

