# # wap print "hello"
# word = "hello"
# for item in word :
#     print(item)
#
#
# # wap print num = [2,3,45,89]
# num = [2,3,45,89]
# for item in num :
#     print(item)


# # wap print num = {2,3,45,89}
# num = {2,3,45,89,}
# for item in num :
#     print(item)


# # wap print num = {'a':2,'b':3,'c':45,'d':89}
# num = {'a':2,'b':3,'c':45,'d':89}
# for item in num :
#     print(item)
#
#
# # wap print to get the following output num = 2,5,8,11,14,17,20 using range function
# for item in range (2,22,3):
#     print(item)


# # wap to print the "python" for 5 times
# word = "python"
# for item in range(5) :
#     print("python")


# wap to extract all the upper case character present inside the given string
# string = input("Enter the words ")
# result = ""
# for item in string :
#     if "A" <= item <= "Z" :
#         result = result+ item
# print(result)


# wap to extract all the integer data present inside the given list collection
# _data = [ 1,23,43,16,4+5j,'hai',4.55]
# _data = [ 1,23,43,16,4+5j,'hai',4.55]
# out = []
# for item in _data:
#     if type(item) == int:
#         out = out + [item]
# print(out)


# # reverse the number and print 10 to 1 using for loop
# for item in range(10,0,-1) :
#     print(item)


# wap to print all the even numbers from 1 to 100
# for item in range (0,101,2):
#     print(item)


# wap to print all the numbers which are divisible by 3 between the range 1 to 100
# for item in range (1,101):
#     if item % 3 == 0:
#         print(item)


# wap to print n natural numbers using for loops
# n = int(input("Enter the numbers "))
# for item in range(0,n,1):
#     print(item)


# # wap to print the multiplication table
# table = int(input("Enter the number "))
# for item in range (0,11,1):
#     print(table, "X", item, "=", table*item)


# # wap to find the sum of n natural number .
# num = int(input("Enter the numbers "))
# sum =0
# for item in range (1,num+1,1):
#     sum = sum + num
# print("sum of first",num,"numbers is ",sum)

#
# # wap to print the product of all the even numbers between the range 1 to 10
# product = 1
# for item in range(1,11,):
#     if item % 2 == 0:
#         product = product*item
# print(product)
#
#
# # wap to find a factorial of a given number
# num = 5
# factorial =1
# for item in range(5):
#     factorial = factorial+item
# print(factorial)


# wap find the sum of all the numbers which are multiple of 3 and divisible by 5 between the range 1 to 100
# sum = 0
# for item in range(1,101):
#     if item % 3 == 0 and item % 5 == 0 :
#         sum = sum + item
# print("sum of 3 and 5 divisible are ", sum)


# wap to find the sum of an individual digits present inside the given integer number if
# the obtained sum is even than print sum as it is, else print the original number .
# num = input("Enter the number ")
# sum = 0
# for item in str(num):
#     sum=sum+int(item)
# if sum%2 == 0 :
#     print(sum)
# else:
#     print(num)


# wap to extract the ascii value of all the upper case value of present at the odd index
# in given string and stored the output into list collection.
# value = input("Enter the values ")
# # value = "SHASHIDHARA"
# _list=[]
# for item in range(0,len(value),1):
#     if "A" <= value[item] <= "Z":
#         _list = _list+[ord(value[item])]
# print(_list)


#wap to get the following output
# string = "python is easy"
# output = "python is easy2"
# string = "python is easy"
# output = ''
# add = 0
# for item in string:
#     if item == " ":
#         add = add + 1
#         output = string+str(add)
# print(output)


# wap to get the following output
# values = (10,[1,2,3],(1,2,3,4),'hello',{10},{1,2,3,4})
# # out = {3:[1,2,3],5:'hello',1:{10}}
# out= {}
# for item in values:
#     if type(item) in [str,list,tuple,set,dict,]:
#         if len(item)%2==1:
#             out[len(item)]=item
# print(out)


# wap to extract all the string data items present inside the given set collection and store
# output into set collection
# data= {10,'hai',3+2j,(1,2,3),'hello'}
# output = set()
# for item in data:
#     if type(item) in [str]:
#         output.add(item)
# print(output)


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



# wap to print the divisors of the given number.
# number = int (input("Enter the number "))
# for item in range(1,number+1,):
#     if number % item ==0 :
#         print(item)








