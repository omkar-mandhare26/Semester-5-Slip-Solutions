class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

class Employee(Person):
    def __init__(self,name, address, salary):
        super().__init__(name, address)
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}")
        print(f"Address: {self.address}")
        print(f"Salary: {self.salary}")

object_list = [
    Employee("Omkar", "Nashik", 99000),
    Employee("Rahul", "Mumbai", 100000),
    Employee("Vijay", "Pune", 105000),
    Employee("Akash", "Pune", 100000),
    Employee("Ravi", "Pune", 100000),
]

print(f"Employee Details: ")
for obj in object_list:
    obj.display()
    print()