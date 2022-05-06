class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_me(self):
        print('{} is {} years old'.format(self.name, self.age))


class Student(Person):
    def __init__(self, name, age, school):
        super().__init__(name, age)
        self.school = school

    def extra_method(self):
        print(f'Extra: {self.school}')

    @property #decorator for property
    def inc_age(self):
        return self.age + 1


me = Student('Cosmin', 17, 'Pitesti')
me.print_me()
me.extra_method()

print(me.inc_age)

#decorators
class Robo:
    @classmethod
    def hello(cls):
        print(cls.__name__)


r = Robo
r.hello()


class Kobo:
    @staticmethod
    def hello():
        print('I am a static method!')


k = Kobo()
k.hello()

#examples decorators
class FixedFloat:
    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return f'<FixedFloat {self.amount:.2f}>'

    #@staticmethod
    @classmethod
    def from_sum(cls, v1, v2):
        return cls(v1+v2)


number = FixedFloat(213.12134)
print(number)

new_number = FixedFloat.from_sum(81.213, 12.9871)
print(new_number)


class Euro(FixedFloat):
    def __init__(self, amount):
        super().__init__(amount)
        self.symbol = '#'

    def __repr__(self):
        return f'<Euro {self.symbol}{self.amount}>'


money = Euro.from_sum(31.21321, 12.2212)
print(money)