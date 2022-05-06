#generators

#def hundred_numbers():
#  nums = []
#  i = 0
#  while i < 100:
#    nums.append(num)
#    i += 1
#  return nums



def hundred_numbers():
  num = 0
  while num < 100:
    yield num
    num += 1

#how to use it
g = hundred_numbers()
print(next(g)) # yields 0
print(next(g)) # yields 1
print(list(g)) # yields [2,3, ... 99]


my_range_obj = range(10)
# next(my_range_obj) - it's not a generator
print(my_range_obj)


#prime generator example
def prime_generator(bound):
    for n in range(2, bound):
        for x in range(2, n):
            if n % x == 0: 
                break
        else:   
            yield n


primer = prime_generator(23)
print(next(primer)) # yields 2 (it is not entering the second for)
print(next(primer)) # yields 3
print(list(primer)) # yields [5, 7, 11, 13, 17, 19]