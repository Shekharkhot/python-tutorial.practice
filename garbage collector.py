# import gc
'''print(gc.isenabled())#True
gc.disable()
print(gc.isenabled())#False
gc.enable()
print(gc.isenabled())#True

__init__(self)

__del__(self): ====> Destructor

    close db connection
    close network connection
    just before destroying an object, GC always calls destructor to perform cleanup activities.'''
import time
import gc
class Test:
    def __init__(self):
        print("Object Initialisation")

    def __del__(self):
        print('Fulfilling last wish and performing cleanup activities...')
gc.disable()
print(gc.isenabled())
t1 = Test()
#t1 = None
time.sleep(10)
print('End of application')















        
