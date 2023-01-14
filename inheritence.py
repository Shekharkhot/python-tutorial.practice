#single inheritance
#single parent
#single child

'''class Parent:
    def m1(self):
        print('parent method')
        
class Child(Parent):
    def m2(self):
        print('child method')

_obj= Child()
_obj.m1()
_obj.m2()


#multi level inheritance

class Parent:
    def m1(self):
        print('parent method')
        
class Child(Parent):
    def m2(self):
        print('child method')

class Childchild(Child):
    def m3(self):
        print('sub child method')


_obj= Childchild()
_obj.m1()
_obj.m2()
_obj.m3()

#hirachial inheritance

class Parent:
    def m1(self):
        print('parent method')
        
class Child1(Parent):
    def m2(self):
        print('child1 method')

class Child2(Parent):
    def m3(self):
        print('sub child2 method')

_obj= Child1()
_obj.m1()
_obj.m2()
print()
Child1=Child2()
Child1.m1()
Child1.m3()

#Multiple inheritance

class Parent1:
    def m1(self):
        print('parent1 method')
        
class Parent2(Parent):
    def m1(self):
        print('Parent2 method')

class Child(Parent1,Parent2):pass

_obj=Child()
_obj.m1()'''

#cyclic inheritance
#class A(A):
#if class extends same class thats y python dont support or
#class A(B):
#class B(A):

# Hybrid Inheritance = single+multiple+multi level+hierarchical

#MRO
#Method Resolution Order
class Parent:
    def m1(self):
        print('Parent Method')
class Child(Parent):pass

print(Child.mro())
#left to right
class A:pass
class B(A):pass
class C(A):pass
class D(B,C):pass
print(A.mro())
print(B.mro())
print(C.mro())    
print(D.mro())
'''
    O
A   B   C
  X   Y
    P
c3 Algorithm
mro(P)= P+Merge(mro(X),mro(Y),mro(C),XYC)
mro(P)= P+Merge(XAB0,YBCO,CO,XYC)
        P+X+Merge(ABO,YBCO,CO,YC)
        P+X+A+Merge(BO,YBCO,CO,YC)
        P+X+A+Y+Merge(BO,BCO,CO,C)
        P+X+A+Y+B+Merge(O,CO,CO,C)
        P+X+A+Y+B+C+Merge(O,O,O)
        P+X+A+Y+B+C+O

'''




















