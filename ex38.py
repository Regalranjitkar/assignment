class Square():
    def __init__(self,s1):
        self.s1 = s1
    def calculate_perimeter(self):
        return self.s1*4
    def __repr__(self):
        print("{} by {} by {} by {}".format(self.s1,self.s1,self.s1,self.s1))
square = Square(5)
square.__repr__()
