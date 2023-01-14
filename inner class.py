class Employee:
    def __init__(self,eno,ename,esal):
        self.eno = eno
        self.ename = ename
        self.esal = esal

    def display(self):
        print('Employee Number:',self.eno)
        print('Employee Name:',self.ename)
        print('Empoyee salary:',self.esal)

class Test:
    def modify(emp):
        emp.esal=emp.esal+10000
        emp.display()

e = Employee(23723,"shekhar",7000)
Test.modify(e)
'''-------------------------------------'''
''' Inner class'''
class Outer:
    def __init__(self):
        print("Outer class object creation...")

    class Inner:
        def __init__(self):
            print("Inner class object creation...")

        def m1(self):
            print("Inner class method")
outer_obj = Outer()  
inner_obj = outer_obj.Inner()
'''inner_obj = Outer().Inner()'''
inner_obj .m1
'''Outer().Inner().m1'''

'''-------------------------------------'''
class Person:
    def __init__(self):
        self.name = 'shekhar'
        self.dob = self.DOB()
    def display(self):
        print('Name:',self.name)
        self.dob.display()

    class DOB:
        def __init__(self):
            self.dd = 15
            self.mm = 5
            self.yyyy=1853
        def display(self):
            print('DOB={}/{}/{}'.format(self.dd,self.mm,self.yyyy))
            
_ob = Person()
_ob.display()



























            

