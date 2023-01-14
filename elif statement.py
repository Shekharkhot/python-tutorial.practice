# #wap to find relation between 2 int numbers
# num_1 = int(input("enter the num_1 "))
# num_2 = int(input("enter the num_2 "))
# if num_1 > num_2:
#     print("num_1 greater than num_2")
# elif num_1 < num_2:
#     print("num_1 is smaller than num_2")


# # waptcw the type of character
# char_ = input("enter the char ")
# if "A" <= char_ <= "Z" :
#     print("UPPER CASE")
# elif "a" <= char_ <= 'z':
#     print("lower case")
# elif "0" <= char_ <= "9":
#     print("Its a numeric")
# else:
#     print("Its a special character")


# # waptcw the given number is single or 2 digit or 3 digits or more than 3 digits or not
# num = int(input('enter the num '))
# if len(str(num)) == 1:
#     print("single digit")
# elif len(str(num)) == 2:
#     print("double digits")
# elif len(str(num)) == 3:
#     print("three digits")
# else:
#     print("more than three digits")

# or
# num = int(input('enter the num '))
# if 0 <= num <= 9:
#     print("single digit")
# elif 10 <= num <= 99:
#     print("double digits")
# elif 100 <= num <= 999:
#     print("three digits")
# else:
#     print("more than three digits")


# # wap to predict the result of the students based on the obtain percentage if it is above 75% then print
# # distinction, if it is lies between 60% to 75% then print first class if it is 50% to 60% second class,
# # from 35 to 50 just pass, else fail
# result = int (input('enter the percentage '))
# if 75 <= result <= 100 :
#     print("distinction")
# elif 60 <= result <= 75 :
#     print("first class")
# elif 50 <= result <= 60 :
#     print("second class")
# elif 35 <= result <= 50 :
#     print("just pass")
# else:
#     print("fail")


# # wap to consider an integer input and print fizz if the number is divisible by 3 and
# # print buzz if the number is divisible 5 print fizz buzz if the number is divisible by both 3 and 5
# play = int(input("enter the number "))
# if play % 3 == 0 and play % 5 == 0 :
#     print("fizz buzz")
# elif play % 3 == 0 :
#     print("fizz")
# elif play % 5 == 0 :
#     print("buzz")
# else:
#     print("enter a valid input")


# wap to find the length of the given string if the length is more than 5 then print all the character are present at odd
# index, if the length is less than 5 then print all the character present at even index, if the length is exactly 5
# then print reversed string
# words = input("enter a word ")
# if len(str(words)) > 5 :
#     print(words[1::2])
# elif len(str(words)) < 5 :
#     print(words[0::2])
# else:
#     print(words[::-1])


# wap to consider an integer input if the number is lies between 2 and 5 than print the product of 2 and 5
# if the number lies between 5 and 7 than print the sum of the 5 and 7 else print a number as it is
# num = int (input("enter the num "))
# if 2 <= num <= 5 :
#     print(2*5)
# elif 5 <= num <= 7 :
#     print(5+7)
# else:
#     print(num)


# wap to find the greater among 3
# num1 = int(input("enter the 1st number "))
# num2 = int(input("enter the 2nd number "))
# num3 = int(input("enter the 3rd number "))
# if num1 > num2 and num1 > num3 :
#     print("num1 is greater")
# elif num2 > num3 :
#     print("num2 is greater")
# else:
#     print("num3 is greater")


# # wap to find the smallest among 5 number
# num1,num2,num3,num4,num5 = int(input("num1 ")),int(input("num2 ")),int(input("num3 ")),int(input("num4 ")),int(input("num5 "))
# if num1<num2 and num1<num3 and num1<num4 and num1<num5:
#     print("num1 is smaller")
# elif num2 < num3 and num2<num4 and num2 < num5:
#     print("num2 is smaller")
# elif num3 < num4 and num3 < num5:
#     print("num3 is smaller")
# elif num4<num5:
#     print("num4 is smaller")
# else:
#     print("num5 is smaller")

            # or

# num1,num2,num3,num4,num5 = int(input("num1 ")),int(input("num2 ")),int(input("num3 ")),int(input("num4 ")),int(input("num5 "))
# if num1 < num2 < num3 < num4 < num5:
#     print("num1 is smaller")
# elif num2 < num3 < num4 < num5:
#     print("num2 is smaller")
# elif num3 < num4 < num5:
#     print("num3 is smaller")
# elif num4 < num5:
#     print("num4 is smaller")
# else:
#     print("num5 is smaller")

