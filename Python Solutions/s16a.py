class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return  (self.length + self.width) * 2  

r = Rectangle(5, 10)
print(f"Area: {r.area()}")
print(f"Perimeter: {r.perimeter()}")