# numbers = [1,2,3,4,5,6]
# squares = []
# for num in numbers:
#     squares.append(num ** 2)
# print(squares)
#
#
# #  using comprehension
# numbers = [1,2,3,4,5,6]
# squares = [num**2 for num in numbers]
# print(squares)
#
#
# numbers = [1,2,3,4,5,6]
# def _squares(numb):
#     return numb ** 2
# _map = map(_squares,numbers)
# result = list(_map)
# print(result)
#
#
# names = ['apple', 'google', 'yahoo', 'gmail', 'facebook', 'yelp', 'microsoft', 'instagram']
# _len_pair = []
# for item in names:
#     _len_pair.append((item,len(item)))
# print(_len_pair)
#
#
# names = ['apple', 'google', 'yahoo', 'gmail', 'facebook', 'yelp', 'microsoft', 'instagram']
# def _len_pair(fruit):
#     return fruit,len(fruit)
#
# _map=map(_len_pair,names)
# output = list(_map)
# print(output)
#
#
# names = ['apple', 'google', 'yahoo', 'gmail', 'facebook', 'yelp', 'microsoft', 'instagram']
# # using lambada function
# _lenpair = map(lambda name:(name,len(name)),names)
# output = list(_lenpair)
# print(output)
#
#
# # using map functions
# names = ['apple', 'google', 'yahoo', 'gmail', 'facebook', 'yelp', 'microsoft', 'instagram']
# def _len_pair(fruit):
#     return fruit,len(fruit)
#
# output = map(_len_pair,names)
# _output = list(output)
# print(_output)
#
#
# str_nums = ["1", "2", "3", "4"]
# # _nums = [int(item) for item in str_nums]
# # print(_nums)
#
#
# _str_nums = ["1", "2", "3", "4"]
# def _strnums(number):
#     return int(number)
# _maps= map(_strnums,_str_nums)
# output= list(_maps)
# print(output)
#
#
# numbers = [-1, -2, -3, -4]
# # p_numbers = [ abs(item) for item in numbers ]
# m_aps= map(abs,numbers)
# output = list(m_aps)
# print(output)
#
#
# a=[1,2,3]
# b=[4,5,6]
#
# def quaderetic_equation(p,q):
#     return p ** 2 + q ** 2 + 2 * p * q
# ans= map(quaderetic_equation,a,b)
# result= list(ans)
# print(result)
#
#
# def quaderetic_equation(num1, num2):
#     return num1 ** 2 + num2 ** 2 + 2 * num1 * num2
#
# x = [1, 2, 3, 4, 5]
# y = [6, 7, 8, 9, 0]
#
# q_numbers = [ quaderetic_equation(n1, n2)  for n1, n2 in zip(x, y)]
#
# # without using "for" loop
# m = map(quaderetic_equation, x, y)
# out= list(m)
# print(out)
#
#
# from math import factorial
# numbers = [1, 2, 3, 4, 5]
# fact = [factorial(number) for number in numbers]
# print(fact)
#
#
# # using map function
# from math import factorial
# number = [1, 2, 3, 4, 5]
#
# _map = map(factorial,number)
# ans = list(_map)
# print(ans)
#
#
