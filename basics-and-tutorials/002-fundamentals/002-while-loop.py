#while statement

i = 0
while i < 10:
    print('iteration ' + str(i))
    i=i+1

is_learning = True
while is_learning:
    print("You're learning")
    user_input = input("Are u still learning? ")
    is_learning = user_input == "yes"