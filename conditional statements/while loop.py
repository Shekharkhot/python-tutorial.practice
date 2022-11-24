# # wap to print the numbers of 1 to 10 using while loop
# num = 1
# while num <= 10 :
#     print(num)
#     num = num + 1


# # wap to print the numbers of 10 to 1 using while loop
# _num = 10
# while _num >= 1 :
#     print(_num)
#     _num = _num-1


# # wap to print the name shekhar rocks rocks rocks rocks 5 times using nested while loop
## while loop
# name = 5
# while name >= 1 :
#     print("shekhar rocks rocks rocks rocks")
#     name = name - 1

    # or

# _name = 1
# while _name <= 5:
#     print("shekhar ", end="")
#     _name = _name+1
#     addition = 1
#     while addition <= 4 :
#         print("Rocks ",end="")
#         addition = addition+1
#     print()


# #Wap to print all the even numbers from 1 to 100
# num = 1
# while num <= 100 :
#     if (num % 2 == 0) :
#       print(num)
#     num = num + 1


# #wap to print all the numbers which are divisible by 3 between the range of 100
# num = 1
# while num <= 100 :
#     if num % 3 == 0 :
#         print(num)
#     num = num + 1


# #wap to print the n natural numbers
# num = 1
# n = int(input("Enter the number "))
# while num <= n :
#     print(num)
#     num = num + 1


# #wap to print the multiplication table
# num = 1
# n = int(input("enter the number "))
# while num <= 10 :
#     print(n,"X",num,"=",n*num,) ## for remove space using (sep = "")
#     num = num + 1


# wap to find the sum of n natural numbers
# num = 1
# n = int(input("Enter the number "))
# result = 0
# while num<=n :
#     result = result + num
#     num = num + 1
# print(result)


# # wap to find the product of all the even numbers between the range 1 to 10
# num = 1
# result = 1
# while num <= 10 :
#     if num % 2 == 0 :
#         result = result * num
#     num = num + 1
# print(result)


# wap to find sum of all the numbers which are multiple of 3 and divisible by 5 between the range 1 to 100
# num = 1
# result = 1
# while num <= 100 :
#     if num % 3 == 0 and num % 5 == 0 :
#         result = result + num
#     num = num + 1
# print(result)


# # wap to find a factorial of a given numbers
# n = int(input("Enter the number "))
# num = 1
# result = 1
# while num <= n :
#     result = result * num
#     num = num + 1
# print(result)


# # wap to print all the integer numbers present in a given list
# list= [1,35,6.8,420,640,"hai"]
# item = 0
# while item < len(list) :
#     if type (list[item]) == int :
#         print(list[item])
#     item = item + 1


# #wap to extract all the vowels present at odd index in a given string
# string = input("Enter the words ")
# item = 1
# while item <len (string) :
#     if string[item] in 'aeiouAEIOU' and item % 2 != 0 :
#         print(string[item],end = " ")
#     item = item + 1


# wap to convert all the upper case character present inside the string in to lower case character
# string =  input("Enter the characters ")
# result = ""
# item = 0
# while item < len(string) :
#     if 'A'<= string[item]<='Z':
#         result = result + chr(ord(string[item]) + 32 )
#     else :
#         result = result + (string[item])
#     item = item + 1
# print(result)


# # wap to convert all the lower case character present at even
# index to uppercase by keeping other characters as it is
# string = input("Enter the characters ")
# result = ""
# item = 0
# while item < len(string) :
#     if "a" <= string[item] <= "z" and item % 2 == 0 :
#         result = result + chr(ord(string[item])-32)
#     else:
#         result = result + (string[item])
#     item = item + 1
# print(result)


# # wap to extract all the float numbers present inside the given list
# list = [1.23,2.3,6,8.3,'hai',6]
# item = 0
# result = []
# while item < len(list) :
#     if type(list[item]) == float :
#         result = result + [list[item]]
#     item = item + 1
# print(result)


# wap to reverse a string without slicing
# words = input("Enter the words ")
# result = ''
# item = 0
# while item > -len(words) :
#     result +=words [item-1]
#     item -=1
# print(result)

#      or

# s = input("Enter the string ") # initial string
# reversedString=''
# index = len(s) # calculate length of string and save in index
# while index > 0:
#     reversedString += s[ index - 1 ] # save the value of str[index-1] in reverseString
#     index = index - 1 # decrement index
# print(reversedString) # reversed string


# # wap to reverse a given integer number without using slicing & type casting
# My_Number = int(input("Please provide the number to be reversed: "))
# Reverse_Number = 0
# while(My_Number > 0):
#  Reminder = My_Number %10
#  Reverse_Number = (Reverse_Number *10) + Reminder
#  My_Number = My_Number //10
# print("Reverse of the provided number is = %d" %Reverse_Number)


# wap to extract all the upper case character,lower case character ,spl character and number
# present inside the string in to 4 different variables respectively .
# string = input("Enter the characters ")
# item = 0
# upper_case,lower_case,numbers,special_character = '','','','',
# while item < len (string):
#     if "A" <= string[item] <= 'Z' :
#         upper_case = upper_case + string[item]
#     elif "a" <= string[item] <= 'z' :
#         lower_case = lower_case + string[item]
#     elif "0" <= string[item] <= '9' :
#         numbers = numbers + string[item]
#     else :
#         special_character = special_character + string[item]
#     item = item + 1
# print(upper_case,lower_case,special_character,numbers, end= " ")


# wap to extract all lower case character present at even index
# string = input('Enter the characters ')
# result = ''
# item = 0
# while item < len(string) :
#     if 'a'<= string[item]<='z' and item % 2 == 0 :
#         result = result + string[item]
#     item = item + 1
# print(result)


# wap to extract all the complex number present inside the given tuple & store the output into tuple collection .
# words = tuple(input('Enter the complex numbers '))
# words = (1.23,2.3,6+5j,8.3,'hai',6+2j)
# _tuple = ()
# item = 0
# while item < len(words) :
#     if type(words[item]) == complex :
#         _tuple = _tuple + (words[item],)
#     item = item + 1
# print(_tuple)


# # wap to find the product of all the integer numbers present inside the given list only
# # if the integer is having minimum 3 digits in it
# list = ['hai', 25, 4, 2.6, 456, 0.1, 2 / 3,111]
# item = 0
# product = 1
# while item < len(list) :
#     if type (list[item]) == int and len(str(list[item]))>=3:
#         product = product * list[item]
#     item = item + 1
# print(product)


# wap to check whether the given number is palindrome or not without using slicing and type casting
# number = int(input("Enter the number "))
# reverse = number
# result = 0
# while (number> 0) :
#     _reminder = number % 10
#     result = result * 10 + _reminder
#     number = number//10
# if reverse == result :
#     print('Its a palindrome')
# else:
#     print("not a palindrome")


# wap to print the given string for 10 times only if its length is exactly equal to  10.
# string = 'aaaaaaaaaa'
# index = 1
# while index <= len(string):
#     if len(string) == 10:
#         print(string)
#     index = index + 1
# else:
#     print('length of char is  not ten')


# wap to find the sum of ASCI value of all the upper case characters
# present inside the string if the sum is even then print the python students are the best else print
# java students are best
# string =input('Enter the string ')
# item = 0
# sum = 0
# while item<len(string) :
#     if type(string[item]) == str and 'A'<= string[item]<='Z' :
#         sum = sum + ord(string[item])
#     item = item  + 1
# if sum%2 ==0 :
#     print('python students are best')
# else :
#     print('java students are best')


# # wap to get the following output
# # string = 'Program'
# # output = 'P0r1o2g3r4a5m6'
# string = input('Enter the character ')
# output = ''
# item = 0
# while item < len(string):
#     output = output + string[item] +str(item)
#     item = item + 1
# print(output)

# wap to print remove space from a given string
# string = input('Enter the string ')
# output = ''
# item = 0
# while item<len(string):
#     if string[item]!=' ':
#         output = output + string[item]
#     item = item + 1
# print(output)


# wap to remove the duplicate values from the given list without using slicing and type casting
# string = input('Enter the string ')
# item = 0
# result = []
# while item<len(string) :
#     if string [item] not in result :
#         result = result+[string[item]]
#     item = item + 1
# print(result)


# # wap to get the following output
# # word = 'h@i_hel!*'
# # output = '@_!*4'
# word = 'h@i_hel!*'
# result = ''
# item = 0
# while item<len(word) :
#     if not ('A'<= word[item] <= 'Z' or 'a'<= word[item] <= 'z' or '0'<= word[item] <= '9') :
#         result = result+ word[item]
#     item = item + 1
# result = result + str(len(result))
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


# wap to extract all the special characters present add odd index
# char = str(input('Enter the characters '))
# item = 0
# result = ""
# while item<len(char):
#     if not("A"<=char[item]<="Z" or "a"<=char[item]<="z" or "0"<=char[item]<="9" or item % 2 == 0):
#         result = result+(char[item])
#     item = item + 1
# print(result)


# wap to find the sum of all the complex number present at inside given tuple
# string = (25+6j,65,2.3,6+4j,25+3j)
# result = 0
# item = 0
# while item<len(string):
#     if type(string[item]) == complex :
#         result = result + string[item]
#     item = item + 1
# print(result)


# wap to check whether the given string is having more than 3 vowels or not if it is having 3 or more than 3 vowels
# than print the vowels else print all the consonants.
# string = input('Enter the number ')
# vowels = ''
# consonents = ''
# item = 0
# while item<len(string):
#     if 'A'<= string[item]<= 'Z' or "a"<=string[item]<= 'z':
#         if string[item] in 'AEIOUaeiou' :
#             vowels = vowels+ string[item]
#         else:
#             consonents = consonents+ string[item]
#         item = item+1
# if len(vowels)>=3 :
#     print(vowels)
# else:
#     print(consonents)


# wap to extract all the upper case character along with its ascii value by considering a given string
# words = input("Enter the words ")
# out = []
# item = 0
# while item< len(words):
#     if 'A'<= words[item]<= 'Z' :
#         out= out+[(words[item],ord(words[item]))]
#     item = item + 1
# print(out)


# string = 'hai hello how are you'
# out = 'hai_hello_how_are_you'
# string = 'hai hello how are you'
# result = ''
# item = 0
# while item<len(string):
#     if string[item] == ' ':
#         result = result + '_'
#     else:
#         result = result+ string[item]
#     item= item + 1
# print(result)


# wap to get the following output
# a = [ 12,'hai',7.8,'hello']
# # out={hai:3 hello:5}
# string = [ 12,'hai',7.8,'hello']
# out = {}
# item = 0
# while item < len(string):
#     if type[string[item]] == str :
#         out[string[item]]=len(string[item])
#     item = item+1
# print(out)


# # wap to get the following output
# string= ['abcd','hai',371,'hello']
# # out= ['abcd','iah',371,'olleh']
# item = 0
# out=[]

# while item<len(string):
#     if item%2 ==0:
#         out= out+[string[item]]
#     else:
#         out= out+[string[item][::-1]]
#     item=item+1
# print(out)

