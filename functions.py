# def sample():
#     variable1 = int(input("Enter the number 1 "))
#     variable2 = int(input("Enter the number 1 "))
#     variables=variable1+variable2
#     return variables
# print(sample())
#
# def sample():
#     variable1 = input("Enter the number ")
#     output= ""
#     for item in variable1:
#         if "0"<=item<="9":
#             output= output+item
#     print(output)
# sample()


# # wap to extract all the lower key character present at even index in a given string
# def even():
#     fruits = input("enter the words ")
#     fruit_char = ""
#     for item in range(len(fruits)):
#         if "a"<=fruits[item]<="z" and item%2==0:
#             fruit_char+=fruits[item]
#     print(fruit_char)
# even()


# wap to find the sum of all the odd int numbers present at even
# index from a given list only if it is having less than 3digits.
# def sam():
#     list_=[12, 44, 331, 6, 1111, 486, 36, 65, 13, ]
#     store = 0
#     for item in range(len(list_)):
#         if list_[item]%2!=0 and len(str(list_[item]))<3:
#             if item % 2==0:
#                 store+=list_[item]
#     print(store)
# sam() # prints 13


# wap to check whether the given number is perfect number or not.
# perfect numbers are [6,28,496,8128]
# def num_perfect():
#     num=int(input("enter the number "))
#     sum_n = 0
#     for item in range(1, num):
#         if num % item == 0:
#             sum_n+=item
#     if sum_n == num:
#         print(sum_n,"is perfect number")
# num_perfect()

# -------------------------------------------------------------------------------------
# function without arguments and with return values
# -------------------------------------------------------------------------------------
# wap to extract all the special character from the given string only if its asci values is even
# def func():
#     spl_char = input("enter the values: ")
#     result = ""
#     for char in spl_char:
#         if not("a"<= char <="z" or "A"<= char <= "Z" or "0"<= char <= "9"):
#             if ord(char) % 2 == 0:
#                 result += char
#     return result
# print(func())


# # wap to check whether the sum of individual digit of a given integer numbers is perfect number or not.
# def _sum():
#     number = int(input("Enter the numbers "))
#     _perfect = 0
#     for num in str(number):
#         _perfect += int(num)
#     output = 0
#     for item in range(1,_perfect):
#         if _perfect % item == 0:
#             output+=item
#     if _perfect == output:
#         return "perfect num "
#     else:
#         return "its not a perfect number"
# print(_sum())


# wap to extract all the string data items present inside and length of
# the string act as key and length of the string should act as value.
# def func():
#     data = [10,'hai','hello',3,5,2+3j,"paython"]
#     output = {}
#     for item in data:
#         if type(item) == str:
#             output[item] = len(item)
#     return output
# print(func())


# wap to get the following output
# _string = "hai hello how are you aa"
# output = {"hai":1,'are':1,"aa":2}
# def sam():
#     _string = "hai hello how are you aa"
#     # _string = input("Enter the words ")
#     output = {}
#     _split = _string.split()
#     for item in _split:
#         if "a" in item:
#             if item.count('a')>=1:
#                 output[item]=item.count('a')
#     return output
# print(sam())
#
# ---------------------------------------------------------------------------------------
# wap to create 4 different function to perform addition subtraction multiplication division respectively
# def calculator(num1,num2):
#     return num1+num2,num1-num2,num1*num2,num1/num2
# print(calculator(10,20))


# wap to get the following output
# word = "abcde2*f $"
# result = 'ace2*$'
# word = "abcde2*f$"
# def sample(word):
#     output = ""
#     for item in range(0, len(word)):
#         if item % 2 == 0 and "a" <= word[item] <= "z":
#             output += ""
#         else:
#             output += word[item]
#     return output
# print(sample(input("enter words: ")))


# wap to print the series of prime number between the range of (1,100)
# def _prime(num):
#     if num == 1:
#         return False
#     for _item in range(2, num):
#         if num % _item == 0:
#             return False
#     return True
# for item in range(1,101):
#     if _prime(item):
#         print(item)


# wap to print all the perfect number between the range of 1,100
# def _perfect(num):
#     _sum = 0
#     for item in range(1, num):
#         if num % item == 0:
#             _sum += item
#     if _sum == num:
#         return True
#     else:
#         return False
# for _item in range(1,101):
#     if _perfect(_item):
#         print(_item)


# wap to check the whether the given number is strong or not by using with argument and with return value.
# (find factorial with arg and rtn val)
# def _fact(num):
#     store=0
#     for item in str(num):
#         store *= int(item)
#     if store != num:
#         print("strong num")
# else:
#     print("not a strong number")
# _fact(int(input("enter the number: ")))














