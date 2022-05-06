#iterators
class FirstHundredGenerator(object):
    def __init__(self):
        self.number = 0

    def __next__(self):
        if self.number < 100:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration()


gen = FirstHundredGenerator()
print(next(gen))  # 0
print(next(gen))  # 1
print(gen.__next__())  # 2


class FirstFiveIterator:
    def __init__(self):
        self.numbers = [1, 2, 3, 4, 5]
        self.i = 0

    def __next__(self):
        if self.i < len(self.numbers):
            current = self.numbers[self.i]
            self.i += 1
            return current
        else:
            raise StopIteration()

#iterator != iterable

#sum(FirstHundredGenerator())

# for i in FirstHundredGenerator():
#     print(i)


class PrimeGenerator:
    def __init__(self, stop):
        self.stop = stop
        self.start = 2

    def __next__(self):
        for n in range(self.start, self.stop):  
            for x in range(2, n):
                if n % x == 0:      
                    break
            else:   
                self.start = n + 1  
                return n    
        raise StopIteration()