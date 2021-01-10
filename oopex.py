class Rectangle:
    def __init__(self,w,l):
        self.width = w
        self.length = l
    def calculate_perimeter(self):
        print(2*(self.width+self.length))
class Square:
    def __init__(self,l):
        self.s1 = l
    def calculate_perimeter(self):
        print(4*self.s1)


rectangle = Rectangle(10,5)
rectangle.calculate_perimeter()
square = Square(3)
square.calculate_perimeter()
        
        
        
