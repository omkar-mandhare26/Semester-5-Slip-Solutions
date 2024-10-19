
class Shape:
    pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def volume(self):
        return self.side * self.side
    

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def volume(self):
        return 3.14 * self.radius * self.radius * self.radius