import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def show(self):
        return f"({self.x}, {self.y})"
    
    def move(self, xmove, ymove):
        self.xmove = xmove + self.x
        self.ymove = ymove + self.y
        return f"({self.xmove}, {self.ymove})"
    
    def dist(self, x0, y0):
        self.x0 = x0
        self.y0 = y0
        return (math.sqrt((self.x0-self.x)**2 + (self.y0-self.y)**2))

        
