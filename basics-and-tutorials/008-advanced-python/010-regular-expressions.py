# regular expressions
import re

email = 'johndoe@goagal.com'
expression = '[a-z]+'

matches = re.findall(expression, email)
print(matches)

name = matches[0]
domain = f'{matches[1]}.{matches[2]}'

# a better approach
email = 'johndoe@goagal.com'
expression = '[a-z\.]+'

matches = re.findall(expression, email)
print(matches)

# or
email = 'johndoe@goagal.com'
print(email.split('@'))

# price
price = 'Price: $189.50'
expression = 'Price: \$(\d+\.\d+)'

matches = re.search(expression, price)
print(matches.group(0))  # entire match
print(matches.group(1))  # first thing around brackets

# with commas
price = 'Price: $11,489.50'
expression = 'Price: \$([\d,]+\.\d+)'

matches = re.search(expression, price)
print(matches.group(0))  # entire match
print(matches.group(1))  # first thing around brackets

# and conversion
num = '11,489.50'

num = num.replace(',', '')  # replace ',' for ''
print(float(num))

def is_filename_safe(filename):
    regex = '^[a-zA-Z0-9][a-zA-Z0-9_()-]*(\.jpg|\.jpeg|\.png|\.gif)$'
    # ^[a-zA-Z0-9]      start with a-zA-Z0-9
    # [a-zA-Z0-9_()-]+      then only contains a-zA-Z0-9_()- for any number of times
    # (\.jpg|\.jpeg|\.png|\.gif)$       at last, it must end with one of the four extensions, remember to escape the dot
    # since we check from start to end, it can either match the whole string or none
    return re.match(regex, filename) is not None