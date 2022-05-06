#numbers
age = 35 #integer
PI = 3.14159 #float

math_operation = 1 + 3 * 4 / 2 - 2
print('the result of 1 + 3 * 4 / 2 - 2 is: ', math_operation)

#division
float_division = 12 / 3
print('the result of 12 / 3 is: ', float_division)

integer_division = 12 // 3
print('the result of 12 // 3 is: ', integer_division)

#remainder
a1 = 14 // 5
remainder = 14 % 5
print('the result of 14 % 5 is: ', remainder)

#strings
hello_world = 'Hello world!'
another_hello = "Hello world!"
mixing = "He said 'Oups, i did it again'!"

#multiline - cand be also used as a multiline comment (without assignation)
a_long_text = """
  what do u think 
  about this type of text 
  ?
"""

print('this is a long text: ', a_long_text)

name = 'Kitty!'
greeting = "Hello, " + name
print('gretings: ', greeting)

#converting to a string
age = 15
print('You are ' + str(age))


#string formating 3.6+
print(f"You are {age}")

name="Batman"
greeting = f"How are you, {name}?" #calculated here, not dynamic
print('hello Dark Knight: ', greeting)

#how to use .format method
final_greeting="How are you, {}?"
paki_greeting = final_greeting.format("Paki")
print(paki_greeting)
zazu_greeting = final_greeting.format("Zazu")
print(zazu_greeting)

final_greeting = "How are you, {name}?"
lucky_greeting = final_greeting.format(name="Lucky")
print(lucky_greeting)

