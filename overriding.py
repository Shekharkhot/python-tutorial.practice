class Parent:
    def property(self):
        print('cash,land,gold,power')

    def marry(self):
        print('sakshi')

class Child(Parent):
    def marry(self):
        #super().marry()  #if both need
        print('rajashri')

call = Child()
call.property()
call.marry()

