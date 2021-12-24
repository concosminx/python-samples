import random

#expression type
print('Type of expression (\'a\') is:', type('a'))
print('Type of expression (2+1.5) is', type(2 + 1.5))

#square root
print('SQRT ', 9**0.5)

#square
print('2^4, ', 2**4)

#strings
a = 'Hello Kitty!'
print('second letter is', a[1]) #0-based
print('last letter is', a[-1])
print('reversed string is', a[::-1])

#lists
list1 = [1,2,3]
print(list1)

list2 = [1]
list2.append(2)
list2.append(3)
print(list2)

#multi dimensional
list3 = [1,2,['another list', 'here']]
print(list3[2])

list4 = [4,3,1,2]
list4.sort()
print('sorted ascending', list4)
list4.sort(reverse=True)
print('sorted descending', list4)

#maps
map = {'key1' : 10, 'key2' : 20}
print('value from map is', map['key2'])
#impbricate
map2 = {'k1' : {'subkey2' : 'actualValue'}}
print('imbricate value is: ', map2['k1']['subkey2'])

#tuple
print('this is a tuple - collection of objects separated by comma', (1, 'alfa', False))

#sets
listWithDuplicates=[1,1,5,6,7,7,7]
print('set ', set(listWithDuplicates))

#booleans
print('value of 3.0 == 3 is ', 3.0 == 3)

#iterative structures - for
subjects = ['I', 'You']
verbs = ['play', 'love']
sports = ['rugby', 'golf']

for subj in subjects:
    for verb in verbs:
        for sport in sports:
            print(subj + ' ' + verb + ' ' + sport)

#generate random list
randomlist = random.sample(range(3, 30, 2), 5)
print('random generated list', randomlist)

