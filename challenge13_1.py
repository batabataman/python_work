

class Shape:
    def who_am_i(self):
        return "I am a shape"

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calcurate_parameter(self):
        return self.width * 2 + self.height *2

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def calcurate_parameter(self):
        return self.length * 4

    def change_size(self, change_size):
        self.length = self.length + change_size

my_rectangle = Rectangle(10, 20)
print(my_rectangle.calcurate_parameter())
print(my_rectangle.who_am_i())
my_square = Square(10)
print(my_square.calcurate_parameter())

my_square.change_size(-3)
print(my_square.calcurate_parameter())
print(my_square.who_am_i())

class Horse:
    def __init__(self, name, rider):
        self.name = name
        self.rider = rider

    def print_rider_name(self):
        print(self.rider.name)

    def get_rider_name(self):
        return self.rider.name

class Rider:
    def __init__(self, name):
        self.name = name

my_rider = Rider("Take Yutaka")
my_horse = Horse("Wodka", my_rider)
my_horse.print_rider_name()
print(my_horse.get_rider_name())
