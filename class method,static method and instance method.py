'''
***classmethod***
class Animal:
    legs = 4
    @classmethod
    def walk(cls,name):
        print('{} walks with {} legs'.format(name,cls.legs))

Animal.walk('dog')
Animal.walk('cat')'''

'''
class Test:
    count =0
    def __init__(self):
        Test.count=Test.count+1

    @classmethod
    def getNoofobjects(cls):
        print('The number of objects created:',cls.count)
t= Test()
t= Test()
t= Test()
t= Test()
Test.getNoofobjects()'''

'''static method'''
class Math:
    
    @staticmethod
    def add(x,y):
        print('The sum is',x+y)

    @staticmethod
    def sub(x,y):
        print('The substraction is',x-y)

    @staticmethod    
    def mul(x,y):
        print('The product is',x*y)

    @staticmethod
    def average(x,y):
        print('The average is ',(x+y)/2)

Math.add(10,20)
Math.sub(50,10)
Math.mul(4,5)
Math.average(50,40)



