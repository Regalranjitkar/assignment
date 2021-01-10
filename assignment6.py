class Shape():
        def what_am_i(self):
                print("I am a Shape.")

class Square(Shape):
        def __init__(self, s1):
                self.s1 = s1
        def calculate_perimetre(self):
                print(self.s1*4)

class Rectangle(Shape):
        def __init__(self,w,l):
                self.w = w
                self.l = l
        def calculate_perimeter(self):
               print(2*(self.w+self.l))

square = Square(5)
square.what_am_i()
square.calculate_perimetre()
rectangle = Rectangle(5,10)
rectangle.what_am_i()
rectangle.calculate_perimeter()
