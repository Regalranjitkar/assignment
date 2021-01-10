class Square():
    square_list = []
    def __init__(self,s1):
        self.s1 = s1
        self.square_list.append((s1))
    def calculate_perimeter(self):
        print (4*(self.s1))
        
square = Square(15)
square_one = Square(20)
square_two = Square(25)
square_one.calculate_perimeter()
print(Square.square_list)
