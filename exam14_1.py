x = 10
class Rectangle:
    recs = []

    def __init__(self, w, l):
        self.width = w
        self.length = l
        self.recs.append((self.width, self.length))
        #global x
        #print(x)
        x = 20
        print(x)

    def print_size(self):
        print("{} by {}").format(self.width, self.length)


my_rect = Rectangle(100, 20)
my_rect2 = Rectangle(100, 20)
print(Rectangle.recs)
print(my_rect.width)
#print(Rectangle.width)
print(type(Rectangle.recs[0]))
print(x)


class Lion:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return self.name

lion = Lion("Dilbert")
print(lion)


class AlwaysPositive:
    def __init__(self, number):
        self.n = number
    def __add__(self, other):
        return abs(self.n + other.n)

x = AlwaysPositive(-300)
y = AlwaysPositive(10)
print(x + y)
