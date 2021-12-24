#guess the number game
import random

attempts = 0

print("Enter your name:")
name = input()

print(name + ', wanna play "Guess the number? (y/n)"')

yes = input()
yes = str(yes)

if yes.upper() == 'Y':
    nr = random.randint(1, 10)
    print('DLH :) ', nr)

    while attempts < 6:
        print("The number between 1 and 10 is: ")
        guess = input()
        guess = int(guess)
        attempts = attempts + 1

        if guess < nr:
            print("Greater")
        if guess > nr:
            print("Lower")
        if guess == nr:
            break
    print(guess)
    print(nr)

    if guess == nr:
        print("Nice job! You guessed the number!")
    else:
        print('Nope. The number I was thinking of was ' + str(nr))
else:
    print("Ok")