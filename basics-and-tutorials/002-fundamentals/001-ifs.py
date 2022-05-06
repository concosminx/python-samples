#if statement
friend = "Cosmin"
user_name = input("Your name: ")

#if-else
if user_name == friend:
    print("Hello, friend!")
    print("Welcome!")
else:
    print("Hello, stranger!")


#if-elif-else
user_name = input("Your name: ")
friends = ["Ube", "Rollo", "Jimmy"]
family = ["Ronnie", "John"]

if user_name in friends:
    print("Hello, friend!")
elif user_name in family:
    print("Hello, family!")
else:
    print("Who are u?")


