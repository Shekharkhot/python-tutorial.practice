                    # break keyword

# range(1,50)
# for item in range (1,50):
#     print(item)
#     if item == 25:
#         break


# for item in range (1,50):
#     print(item)
#     break


# for item in range(1,50):
#     break
#     print(item)
#     # this code is unreacheable


# # # # # wap to ask the user to enter the proper username , until the user enters proper username
# # # # # keep on asking same thing if the user enters the proper username than come out from the loop.
# bank_id = "shekhar"
# while True:
#     username = input("Enter the username ")
#     if bank_id == username:
#         print("Entered username is correct")
#         break
#     else:
#         print("Enter the proper username ")

# # # # wap to guess the original numbers
# # # # original_number = 10
# while True:
#     num = int(input("Enter the number "))
#     if original_number==num:
#         print("Congrats!!! you have guessed the correct number ")
#         break
#     elif num > original_number:
#         print("Entered num is greater than original number")
#     else:
#         print('Please enter the correct number' )


# # wap to print the initial index of a specified character from a given string
# string = input("Enter the string ")
# looking_for = input("Enter the looking for character ")
# # _string = input("Enter the original string ")
# for item in range(0,len(string)):
#     if looking_for==str[item]:
#         print(item)
#         break


# wap to check whether the given string is having only lower case alphabets or not
# my_string = input("Enter the words ")
# for item in my_string:
#     if not("a"<= item<= "z"):
#         print("These are not lower case alphabets")
#         break
# else:
#     print('These are lower case alphabets')


# ###           whileloop break examples


# # wap to check whether the given string is having only lower case alphabets or not
# my_string = input("Enter the words ")
# item = 0
# while item <len(my_string):
#     if not("a" <= my_string[item]<= "z"):
#         print("These are not lower case alphabets")
#         break
#     item = item +1
# else:
#     print('These are lower case alphabets')


# # wap to check whether the given list is having only integer number are not
# _list = [25,6.5,8,3]
# store = []
# # list= input("Enter the values")
# for item in _list:
#     if type[_list] ==store[int]:
#         # store=store,[item]
#         print("wow it has only int values")
#         break
# else:
#     print("Sorry don't have only int values")


# wap to check whether the given set is homogeneous or heterogeneous
# data = {1,2,34,32,24,5.5}
# _store = list(data)
# for item in data :
#     if type(item)!=type(_store[0]):
#         print("Heterogeneous")
#         break
# else:
#     print("Homogeneous")


# wap to check the whether the given number is prime or not
# num = int(input("Enter the number "))
# if num == 1 :
#     print("Neither prime nor composite")
# else:
#     for item in range(2,num):
#         if num % item == 0:
#             print("Not prime")
#             break
#     else:
#         print("Its a prime")

                    # continue keyword

# wap to print all the upper case character present inside the given string using continue.
# data = input("Enter the names ")
# output = ''
# for item in data:
#     if "a"<= item <= "z":
#         continue
#     output = output + item
# print(output)

# wap to extract all the integer number present inside the given set collection by using continue
# variable = {25,5,5.2,"hai",6,333.333}
# _set = set()
# for item in variable :
#     ### if type(item) in {str,list,dict,tuple,set,float,complex}:
#     if type(item)!=int:
#         continue
#     _set.add(item)
# print(_set)


# wap to extract all the characters present at odd index in a given string.
# names = input("Enter the characters ")
# string = ""
# for item in range(0,len(names)) :
#     if item % 2 ==0:
#         continue
#     string = string + names[item]
# print(string)


# wap to extract the key value pair from the dictionary only if the value is of string type
# class = {"age":34,"name":'shekhar',"id":'shekhar123',"mob":8090100}
# result = {"name":'shekhar',"id":'shekhar123'}
# _class = {'age':34,"name":'shekhar',"id":'shekhar123','mob':8090100}
# result = {}
# out = {}
# for item in _class:
#     if type (out[item]) != str:
#         continue
#     result[item] = (out[item])
# print(result)


#               pass keyword

# if 2 < 10:
#     pass
# if 10<20:
#     print('hello')



# wap to convert all upper case characters into lower case and lower case into upper case
# and convert all num and special characters in to space.
# string = input("Enter the string ")
# output = ""
# for item in string :
#     if "A"<=item<="Z":
#         output = output + chr(ord(item)+32)
#     elif "a"<=item<="z":
#         output = output+ chr(ord(item)-32)
#     else:
#         output=output+ ""
# print(output)


