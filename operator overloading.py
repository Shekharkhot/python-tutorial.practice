class BOOK:
    def __init__(self,pages):
        self.pages = pages
        
    def __add__(self,other):
        return self.pages+other.pages


a1 = BOOK(100)
a2 = BOOK(200)
a3 = BOOK(300)
a4 = BOOK(400)
print(a1+a2)
print(a2+a4)


class TBOOK:
    def __init__(self,pages):
        self.pages = pages
    
    def __str__(self):
        return "The no of pages:"+str(self.pages)

    def __add__(self,other):
        total = self.pages+other.pages
        b = TBOOK(total)
        return b

    def __mul__(self,other):
        total = self.pages*other.pages
        b = TBOOK(total)
        return b

b1 = TBOOK(100)
b2 = TBOOK(200)
b3 = TBOOK(300)
b4 = TBOOK(400)
print(b1+b2)
print(b3+b4+b3+b4)
print(b1*b2)
print(b3+b1*b4+b2)

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary = salary

    def __mul__(self,other):
        return self.salary*other.days

class Timesheet:
    def __init__(self,name,days):
        self.name=name
        self.days=days
    def __mul__(self,other):
        return self.days*other.salary

e = Employee('shekhar',500)
t = Timesheet('shekhar',50)
print('This Month salary is :',e*t)
print('This Month Salary is :',t*e)









    







