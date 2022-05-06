#import class from file in the same directory
from adition import Addition

class Calculator:

    @classmethod
    def add(cls, num1, num2):
        return Addition.add(num1, num2)

    @classmethod
    def subtract(cls, num1, num2):
        return cls.add(num1, -num2)

    @classmethod
    def multiply(cls, num1, num2):
        res = 0
        for x in range(0, num2):
            res = cls.add(res, num1)
        return res

    @classmethod
    def divide(cls, num1, num2):
        res = 0
        while num1 >= num2:
            num1 = cls.subtract(num1, num2)
            res = cls.add(res, 1)
        return res
