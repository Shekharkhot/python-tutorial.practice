class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        #100 properties

class Student(Person):
    def __init__(self,name,age,rollno,marks):
        super().__init__(name,age)
        self.rollno=rollno
        self.marks=marks

class Teacher(Person):
    def __init__(self,name,age,salary,subject):
        super().__init__(name,age)
        self.salary=salary
        self.subject=subject
s = Student('ravi',23,121,90)
p = Teacher('ram',54,34334,'python')
