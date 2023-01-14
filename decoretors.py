# from time import sleep, time
# def func():
#     print('Function')
# def wrapper(func):
#     print("Hello")
#     func()
#     print('Thank you')
#
# def function_genertaor():
#     def new_function():
#         print('Its a new function')
#     return new_function
# wrapper(func)
#
# new_func= function_genertaor()
# new_func()


# def decorator(func):
#     def wrapper():
#         print('decorator begins')
#         func()
#         print('decoration ends')
#     return wrapper
# def func():
#     print('Function')
#
# new_func = decorator(func)
# new_func()


# def decorator(func):
#     def wrapper():
#         print('decorator begins')
#         func()
#         print('decoration ends')
#     return wrapper
# @decorator
# def func():
#     print('Function')

# # new_func = decorator(func)
# func()
#

# import time
# def decorator(func):
#     def wrapper():
#         print('decorator begins')
#         func()
#         print('decoration ends')
#     return wrapper
#
# def duration_decorator(func):
#     def wrapper():
#         start_time = time.time()
#         func()
#         duration = time.time()-start_time
#         print(f"duration time is {duration}")
#     return wrapper
# @decorator
# @duration_decorator
# def new_func():
#     print("function")
#     time.sleep(1)
# new_func()


# def decorator(func):
#     def wrapper(wrapper_parameter):
#         print('decorator begins')
#         func(wrapper_parameter)
#         print('decoration ends')
#     return wrapper
# @decorator
# def func(func_parameter):
#     print(func_parameter)
# # func = decorator(func)
# func('something')


# def decorator(func):
#     def wrapper(*args,**kwargs):
#         print('decorator begins')
#         func(*args,**kwargs)
#         print('decoration ends')
#     return wrapper
# @decorator
# def func(func_parameter):
#     print(func_parameter)
# # func = decorator(func)
# func('something')
#

# def repetition_decorator(repetition):
#     def decorator(func):
#         def wrapper():
#             for item in range(repetition):
#                 func()
#         return wrapper
#     return decorator
# @repetition_decorator(20)
# def func():
#     print('function')
# func()

# decorators inside class and @property

# class Generic:
#     def __init__(self):
#         self.x = 10
#     def getx(self):
#         print('getting the x')
#         return self.x
# generic = Generic()
# print(generic.getx())


# @property

# class Generic:
#     def __init__(self):
#         self._x = 10
#     def getter(self):
#         print('get the x')
#         return self._x
#     def setter(self,value):
#         print('set the x')
#         self._x = value
#     def deleter(self):
#         print('delete the x')
#         del self._x
#
#     x = property(getter,setter,deleter)
# generic = Generic()
# generic.x = 4
# print(generic.x)
# del generic.x

# from datetime import datetime  #essential or mandatory
# class Generic:
#     def __init__(self):
#         self._x = 10
#     @property
#     def x(self):
#         print(datetime.now())
#         return self._x
#     @x.setter
#     def x(self,value):
#         print('set the x')
#         self._x = value
#     @x.deleter
#     def x(self):
#         print('delete the x')
#         del self._x
#
# generic = Generic()
# generic.x = 4
# print(generic.x)
# del generic.x

#
# def log(some_other_func):
#     def wrapper(*args, **kwargs):
#         # this is the extra functionality that the decorator is adding
#         print(f"Hey there You called {some_other_func.__name__} function")
#         # actual function is getting executed here
#         result = some_other_func(*args, **kwargs)   # original add(1, 2) func
#         # add(a=1, b=2)
#         return result
#     return wrapper
# @log
# def decorated():
#     print("You did good job")
# decorated()












