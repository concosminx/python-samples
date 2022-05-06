#how to define a class
class Line:
    def __init__(self, coordinate1, coordinate2): # self, similar to this in java
        self.coordinate1 = coordinate1
        self.coordinate2 = coordinate2

    def distance(self):
        x1, y1 = self.coordinate1
        x2, y2 = self.coordinate2
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    def slope(self):
        x1, y1 = self.coordinate1
        x2, y2 = self.coordinate2
        return (y2 - y1) / (x2 - x1)


coord1 = (3, 2)
coord2 = (8, 10)
li = Line(coord1, coord2)

print('distance is: ', li.distance())
print('slope is:', li.slope())


class Cylinder():
    pi = 3.14

    def __init__(self, height, radius):
        self.height = height
        self.radius = radius
        self.base_aria = self.pi * radius ** 2

    def volume(self):
        h = self.height
        r = self.radius
        return self.base_aria * h

    def surface_area(self):
        h = self.height
        r = self.radius
        return (2 * self.base_aria) + (2 * self.pi * r * h)


c = Cylinder(2, 3)
print('volume is: ', c.volume())
print('surface are is: ', c.surface_area())
