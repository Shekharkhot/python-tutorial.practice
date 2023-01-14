# """
# 1. The scope of a variable in python is depends on where the value for the variable
#    is assigned in your source code.!!
# 2. variables assigned inside a function can only be seen by the code within that function.
#    You cannot even refer to such variables from outside the function.
# 3. variables assigned inside a function do not clash with variables outside the function,
#    even if the same variable names are used elsewhere. A variable named 'X' assigned outside a given function
#    (i.e., in a different function or at the top level of a module file)
#    is a completely different variable from a name X assigned inside that function.
# """
# # Global variable
# a = 10
# b = 20
#
# def func():
#     return a + 1  # Prints message at global scope
#
# def func():
#     # the value for b is assigned inside the function
#     b = 20  # Local Variable
#     # the value for a is assigned outside the function
#     return a + b   # a refers to value 10 which is Global variable
#
# def func():
#     # the value for a and b are assigned inside the function. So a and b are local variables
#     a = 20  # a is a local variable.
#     b = 20  # b is a local Variable
#     return a + b
#
# def func():
#     # Local Variable "a"!
#     # A variable can be either local or global variable but not both
#     result = a + b  # Exception! (a will not refer to Global value 10)
#     a = 20
#     b = 30
#     result = a + b
#     return result
# func()
#
# # Raises Exception!
# """
# Traceback (most recent call last):
#   File "<pyshell#9>", line 1, in <module>
#     func()
#   File "<pyshell#8>", line 4, in func
#     result = a + b  # Exception! (a will not refer to Global value 10)
# UnboundLocalError: local variable 'a' referenced before assignment
# """
#
# def func():
#     # the values for a and b are assigned inside the function.
#     # So, 'a' and 'b' are considered as local vairables and not globals
#     a = a + 1
#     b = b + 1
#     return a + b
#
# # Raises Exception!
# """
# Traceback (most recent call last):
#   File "<pyshell#5>", line 1, in <module>
#     func()
#   File "<pyshell#4>", line 4, in func
#     a = a + 1
# UnboundLocalError: local variable 'a' referenced before assignment
# """
# func()
#
# # UnboundLocalError is also caused when you try to assign a variable before assigining an initial value to it.
# # Example:
# def func():
#     a = a + 1       # Adding 1 to un-initlised variable 'a'
#
# def func():
#     # Local "a" to func and enclosing scope for wrapper
#     a = 20
#     def wrapper():
#         # Local "a" to wrapper
#         a = 30
#         return a + 1
#     return wrapper()
#
# def func():
#     # local for func
#     a = 10
#     def wrapper():
#         a = a + 1
#         a = 500
#     return wrapper()
#
# func()
#
# # Raises Exception!
# """
# Traceback (most recent call last):
#   File "<pyshell#5>", line 1, in <module>
#     func()
#   File "<pyshell#4>", line 4, in func
#     a = a + 1
# UnboundLocalError: local variable 'a' referenced before assignment
# """
# # len = "Global variable len"
# def func():
#     # Local "a" to func and enclosing scope for wrapper
#     # len = "local len of func"
#     def wrapper():
#         # Local "a" to wrapper
#         # len = "local len of wrapper"
#         print(len)
#     return wrapper()
#
# # UnboundLocalError is also caused when you try to assign a variable before assigining an initial value to it.
# def func():
#     # Declaring that the variable that you are referring to is global variable
#     global a  # Refers to Global Variable "a"
#     a = 20
#     print(a)
# # --------------------------------------------------------------------------------
# # variables inside comprehension will have its own scope.
# number = -5
# numbers = [ number for number in range(1, 8) ]
# # prints -5
# print(number)
# # --------------------------------------------------------------------------------
# """
# 1. In case of classes, when you look up for an attribute "message",Python tries to look for that attribute on the instance.
# 2. If the attribute exist on the instance, then it will return the value of the instance attribute.
# 3. If the attribute does not exist on the instance, it will lookup for the attribute at class level.
# 4. If the attribute exist on the class level, it will return the value of the class attribute.
# 5. If the attribute does not exist on instance and at class level,then attribute error is raised.
# """
# class Spam:
#     message = "Hello world"
#     def __init__(self):
#         self.message = "Hello universe"
#
# s = Spam()
# print(s.message)   # Prints "Hello universe"
#
# class Spam:
#     message = "Hello world"
#     def __init__(self):
#         self.x = 10
#         self.y = 20
#
# s = Spam()
# print(s.message)    # Prints "Hello world"
#
# # -------------------------------------------------------------------------------------------------
# # Global variable
# a = 10
#
# def spam(number):
#     number = number + 1
#     print(number)
#
# # Passing a immutable object to the function
# # in this case python acts as call by value
# spam(a)
# print(a)
# # ---------------------------------------------------
# a = [10]
#
# def spam(numbers):
#     numbers = numbers.append(11)
#     print(numbers)
#
# # Passing a mutable object to the function
# # in this case python acts as call by reference
# spam(a)
# print(a)