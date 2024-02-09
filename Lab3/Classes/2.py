class Shape():
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, len):
        self.length = len
    def area(self):
        return self.length ** 2
        
