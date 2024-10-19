class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
    
    def __add__(self, other):
        return Circle(self.radius + other.radius)

Circle1 = Circle(5)
Circle2 = Circle(3)

Circle3 = Circle1 + Circle2
print(Circle3.area())