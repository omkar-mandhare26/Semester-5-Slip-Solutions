class BasicCalculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

calc = BasicCalculator()
try:
    print("Addition (5 + 3):", calc.add(5, 3))          
    print("Subtraction (5 - 3):", calc.subtract(5, 3))  
    print("Multiplication (5 * 3):", calc.multiply(5, 3)) 
    print("Division (5 / 3):", calc.divide(5, 3))      
    print("Division (5 / 0):", calc.divide(5, 0))      
except ValueError as e:
    print(e)
