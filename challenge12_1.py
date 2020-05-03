import math
class Apple:
    def __init__(self, s, p, c, w):
        self.size = s
        self.price = p
        self.color = c
        self.weight = w


class Circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        #return math.pow(self.radius,2) * math.pi
        return self.radius ** 2 * math.pi


class Triangle:
    def __init__(self, h, w):
        self.height = h
        self.width = w
    def area(self): 
        return self.width * self.height  / 2

class Hexagon:
    def __init__(self, l1, l2, l3, l4, l5, l6):
        self.length1 = l1
        self.length2 = l2
        self.length3 = l3
        self.length4 = l4
        self.length5 = l5
        self.length6 = l6
    def calcurate_parameter(self):
        return self.length1 + self.length2  + self.length3 + self.length4 + self.length5 + self.length6
    
a = input("please input.")
ci = Circle(int(a))
print(ci.area())

a = input("please input height.")
b = input("please input width")
tri = Triangle(int(a), int(b))
print(tri.area())


hex = Hexagon(1, 2, 3, 4, 5, 6)
print(hex.calcurate_parameter())

