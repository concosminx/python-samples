#read from file
my_file = open('001-data.txt', 'r')
file_content = my_file.read()

my_file.close()

#write to file (overwrite current value)
print(file_content)

user_name = input('Enter your name: ')

my_file_writing = open('001-data.txt', 'w')
my_file_writing.write(user_name)

my_file_writing.close()