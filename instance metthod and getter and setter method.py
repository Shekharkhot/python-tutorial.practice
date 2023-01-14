class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Hi",self.name)
        print("Your Marks Are",self.marks)

    def grade (self):
        if self.marks>=60:
            print("You Got First Grade")
        elif self.marks>=50:
            print("You Got Second Grade")
        elif self.marks>=35:
            print("You Got Third Grade")
        else:
            print("You are Failed")
n = int(input("Enter The Number of Students:"))
for item in range (n):
    name = input("Enter Student Name:")
    marks = int(input("Enter The Student Marks:"))
    s = Student(name,marks)
    s.display()
    s.grade()
    print('*'*30)
