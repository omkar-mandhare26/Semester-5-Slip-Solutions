class Student:
    def __init__(self, sname, marks):
        self.sname = sname
        self.marks = marks

    def display(self):
        print(f"Student Name: {self.sname}")
        print(f"Marks: {self.marks}")

student = Student("Martin", 99) 

print("Original values:")
student.display()

student.sname = "Tim"
student.marks = 92

print("New values:")
student.display()
