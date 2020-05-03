class Shape:
    def what_am_i(self):
        print("I am a shape.")

class Square(Shape):
    square_list = []
    wide_value = ""

    def what_am_i(self):
        super().what_am_i()
        print("I am a square")
        
    def __init__(self, w):
        self.width = w
        self.square_list.append(self.width)
        self.wide_value = "bbb"

    def __repr__(self):
        return "{} by {} by {} by {}".format(self.width, self.width, self.width, self.width)


        

def compare_object(own, other):
    return  own is other

s1 = Square(10)
s2 = Square(30)
print(Square.square_list)
print(Square.wide_value)
print(s1)
a = s1
print(compare_object(s1, a))
print(compare_object(s1, s2))

s1.what_am_i()
