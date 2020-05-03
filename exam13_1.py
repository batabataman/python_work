class Data:
    def __init__(self):
        self.nums  = [1, 2, 3, 4, 5]

    def change_data(self, index, n):
        self.nums[index] = n

data_one = Data()
data_one.nums[0] = 100
print(data_one.nums)

data_two = Data()
print(data_two.nums)

data_two.change_data(2, 200)
print(data_two.nums)


class Shape:
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def print_size(self):
        print("{} by {} = {}".format(self.width, self.len , self.width * self.len))

class Square(Shape):
    def area(self):
        return self.width * self.len
    def print_size(self):
        print("Square {} by {} = {}".format(self.width, self.len , self.width * self.len))

my_shape = Square(3, 4)
my_shape.print_size()
print(my_shape.area())


class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

class Person:
    def __init__(self, name):
        self.name = name

mick = Person("Mick Jagger")

my_dog = Dog("pochi", "B", mick)

print(my_dog.owner.name)
