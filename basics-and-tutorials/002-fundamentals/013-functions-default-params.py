def add(x, y=3):
    total = x + y
    print(total)


add(5)
add(2, 6)
add(x=3)
add(x=5, y=2)

# add(y=2)  # ERROR!
# add(x=2, 5)  # ERROR!


print(1, 2, 3, 4, 5, sep=" - ")  # default is " "

default_y = 3

def add(x, y=default_y):
    sum = x + y
    print(sum)


add(2)  # 5

default_y = 4
print(default_y)  # 4

add(2)  # 5