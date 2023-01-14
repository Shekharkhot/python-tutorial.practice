# wap to split the given string into numbers of sub string store the output into list collection
# string= "hai hello good morning"
# output = ["hai","hello",'good','morning']

# string = 'hai hello good morning'
# # string = input('Enter the words ')
# result = [ ]
# output = ""
# for item in string :
#     if item !='':
#         output+=item
#     else:
#         result =[output]
#         output = ' '
# result+=(output)
# print(result)


# wap to check whether the given string is palindrome or not without slicing, only if length of the string is
# exactly equal to 5
# string = input('Enter the string ')
# string = 'ramar'
# item = 0
# result = ''
# if len(string) == 5:
#     while item<len(string):
#         result = chr((len(string)-1)-item)
#     item = item + 1
# else :
#     print('string has not a 5 character')
# if item==result :
#     print("its a palindrome")
# else:
#     print('its not a palindrome')


# # wap to check whether the given list is having only integer number are not
# _list = [25,63,3,3.2]
# store=[]
# # list= input("Enter the values")
# for item in _list:
#     if type(_list[item]) in [int]:
#         store=store+[item],
#         print("Sorry don't have only int values")
#         break
#     else:
#         print("wow it has only int values")


# # wap to print the initial index of a specified character from a given string
# string = input("Enter the string ")
# looking_for = input("Enter the looking for character ")
# # _string = input("Enter the original string ")
# for item in range(0,len(string)):
#     if looking_for==str[item]:
#         print(item)
#         break


# wap to extract the key value pair from the dictionary only if the value is of string type
# class = {"age":34,"name":'shekhar',"id":'shekhar123',"mob":8090100}
# result = {"name":'shekhar',"id":'shekhar123'}
# _class = {'age':34,"name":'shekhar',"id":'shekhar123','mob':8090100}
# result = dict()
# out = {}
# for item in _class:
#     if type (_class[item]) != {str}:
#         continue
#     out[item] = [result[item]]
# print(out)




