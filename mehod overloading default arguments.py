#default arguments

class Test:
    def sum(self,a= None,b=None,c=None):

        if a!= None and b!= None and c!= None:
            print('The sum of 3 numbers:',a+b+c)

        elif a!= None and b!= None:
            print('The sum of numbers:',a+b)

        else:
            print('please provide 2 or 3 argumnts')

t = Test()
t.sum(10,20,30)
t.sum(10,20)
t.sum(10)

#variable length arguments

class Test:
    def sum(self,*a):
        total = 0
        for item in a:
            total = total+item
        print('The sum :',total)
    
t = Test()
t.sum(10,20)
t.sum(10,20,30,40,)
t.sum(10,20,30,40,50,60)
t.sum()
t.sum(10)

















