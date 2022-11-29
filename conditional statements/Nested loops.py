#                       Nested loops
# for item in range(1,5,2):
#     for jet in range (0,4):
#         print(item,jet)


# for item in range (1,10,3):
#     for jet in range(3,8):
#         print(item,jet,item+jet,item-jet)


# wap count the num of vowels present inside a string from the given list collection
# string = ["abcd",10,23,"helloi",6+5j]
# output = []
# for item in string:
#     if type(item) == str:
#         count = 0
#         for jet in item :
#             if jet in "AEIOUaeiou":
#                 count = count +1
#         output = output + [count]
# print(output)


# wap to check the given number is prime or not
# _number = int(input("Enter the number "))
# for item in range(2,_number+1) :
#     if _number % item !=0:
#         print(" Entered number is prime")
#     else :
#         print("Entered number is not prime")


#  in while

# wap to print all the values which are present inside nested collections,
# the nested collections are present inside a heterogeneous.
# _word = [50,"star",5+6j,[2,4,6],True,{3j,4j,5j}]
# for item in _word:
#     if type(item)in [str,list,dict,set,tuple]:
#         for jet in item:
#             print(jet,end ="' '")


# wap to count the number vowels present inside the strings which are present inside the homogeneous set collection
# the number of vowels must be stored inside the list
# _set = {"rahul",'sachin',"shashii","shekhar"}
# _list =[]
# for item in _set:
#     if type(item) == str:
#         count = 0
#         for jet in item:
#             if jet in "AEIOUaeiou":
#                 count = count+1
#         _list = _list + [count]
# print(_list)


# # wap to extract all the prime numbers in to list between the range 2,n
# _num = int(input("Enter the numbers "))
# result = []
# for item in range(2,_num+1):
#     for jet in range(2,_num):
#         if item % jet ==0:
#             break
#     else:
#         result.append(item)
# print(result)


# letters = "aabcdacccdaaccdbbbacbb"
# count_letter = {'a':6,'b':6,'c':7,'d':3}
# letters = "aabcdacccdaaccdbbbacbb"
# count_letter = {}
# for item in letters:
#         count = 0
#         for jet in letters :
#             if item==jet:
#                 count = count + 1
#                 count_letter[item] = count
# print(count_letter)


# numbers = '1123332123421434'
# output = {"1":4,"2":4,"3":5,"4":3}
# numbers = '1123332123421434'
# output = {}
# for item in numbers :
#     count = 0
#     for jet in numbers :
#         if item == jet:
#             count = count + 1
#             output[item] = count
# print(output)


# wap to store the sum of individual digits of all the integer numbers between the range from 20 to 50 in to a tuple
# store = ()
# for item in range (20,50):
#     _num = 0
#     sum = 0
#     while (item>0):
#         _num = item % 10
#         sum = sum +_num
#         item = item //10
#     store = store+(sum,)
# print(store)


# wap to validate the given password .in order to validate there are set of conditions
# the password must contain of min 8 char the password must have at least one upper character
# alphabet also one lower case, numeric and special character among &,$,@ .
# password = input("Enter the password ")
# for item in password:
#     if len(password)>=8:
#         upper,lower,numeric,special =0,0,0,0
#         for character in password:
#             if "A"<= character<= "Z":
#                 upper = upper+1
#             elif "a"<= character<="z":
#                 lower = lower + 1
#             elif "0"<=character<= "9":
#                 numeric = numeric + 1
#             elif character in "@&$":
#                 special = special+1
#         if upper >=1 and lower >=1 and numeric>=1 and special>=1:
#             print("it is valid password")
#         else:
#             print( "its not valid password")


# wap to get the  following output
# word = "hai ihello"
# # output = {"hai":["hai",3,2],"ihello":["ihello",6,3]}
# output= {}
# string = word.split()
# for item in string:
#     count = 0
#     for jet in item:
#         if jet in "aeiouAEIOU" :
#             count = count +1
#         output[item]=[item,len(item),count]
# print(output)


# wap to get following output
_list = [1,2,45,'opTiON',[1,2],'FoRMat']
# output=[("opTioN",'TON'),('FoRmat','FRM')]
output = []
for item in _list:
    if type(item)== str:
        result = ""
        for jet in item:
            if "A"<= jet<= "Z":
                result = result + jet
        output =output+[(item,result)]
print(output)


