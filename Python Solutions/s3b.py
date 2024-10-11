class Student:
    def __init__(self,rollNo,name,age,gender):
        self.rollNo = rollNo
        self.name = name
        self.age = age
        self.gender = gender

    def displayStudent(self):
        print(f"\nStudent Roll No: {self.rollNo}")
        print(f"Student Name: {self.name}")
        print(f"Student Age: {self.age}")
        print(f"Student Gender: {self.gender}")
    
class Test(Student):
    def __init__(self,rollNo,name,age,gender,marks):
        super().__init__(rollNo,name,age,gender)
        self.marks = marks
    
    def calculateTotalMarks(self):
        sum = 0
        for mark in self.marks.values():
            sum += mark
        
        return sum

    def display(self):
        super().displayStudent()
        print(f"Total Marks: {self.calculateTotalMarks()}")

student1 = Test(20,"Omkar",21,"MALE",{"subject1": 90,"subject2": 89, "subject3": 85})
student2 = Test(38,"Vedant",20,"MALE",{"subject1": 85,"subject2": 81, "subject3": 83})
student3 = Test(18,"Noor",20,"FEMALE",{"subject1": 93,"subject2": 85, "subject3": 80})

student1.display()
student2.display()
student3.display()