class Student:
    def setName(self,name):
        self.name = name

    def getName(self):
        return self.name

    def setMarks(self,marks):
        self.marks = marks

    def getMarks(self):
        return self.marks

    
n = int(input("Enter The Number of Students:"))
for item in range (n):
    name = input("Enter Student Name:")
    marks = int(input("Enter The Student Marks:"))
    s= Student()
    s.setName(name)
    s.setMarks(marks)
    print ('Hi',s.getName())
    print('Your Marks are:',s.getMarks())
    print ('*'*30)
