"""
1. List comprehensions is a way to build lists from sequences or
    any other iterable type by filtering and transforming items.

2. The general syntax for a list comprehension is as follows:
    [expression for item in iterable if condition]
"""
# import math

# numbers = [1,2,3,4,5,6]
# store =[]
# for num in numbers:
#     store.append(num**2)
# print(store)


# List Comprehension # general syntax of list comprehension
# [ expression   for item in some_iterable ]

# Square Numbers in the list. Using List 4_Comprehensions
# numbers = [1,2,3,4,5,6]
# _squares = [num**2 for num in numbers]
# print(_squares)

# List of even numbers between range 1-20
# evens = []
# for num in range(1,20):
#     if num % 2 == 0:
#         evens.append(num)
# print(evens)

# # using list configuration
# _list=[num for num in range(1,30) if num % 2 == 0]
# print(_list)

# Returns a list containing all vowels in the given string
# i want list of strings that starts with vowel character

# names = ['laura', 'steve', 'bill', 'james', 'bob', 'greig', 'scott', 'alex', 'ive']
# store = []
# for item in names:
#     if item[0] in "aeiou":
#         store.append(item)
# print(store)

# using comprehension (Pythonic way or pythonic code)
# _list_strings = [item for item in names if item[0] in "aeiou"]
# print(_list_strings)

# Filtering all the languages which starts with 'p'

# languages = ['Python', 'Java', 'Perl', 'PHP', 'Python', 'JS', 'C++', 'JS', 'Python', 'Ruby']
# # store = []
# # for item in languages:
# #     if item[0] == "P":
# #         store.append(item)
# # print(store)
#
# languages = ['Python', 'Java', 'Perl', 'PHP', 'Python', 'JS', 'C++', 'JS', 'Python', 'Ruby']
# # using list comprehension
# _filtering = [language for language in languages if language[0] == "P"]
# print(_filtering)

# names = ['laura', 'steve', 'bill', 'james', 'bob', 'greig', 'scott', 'alex', 'ive']
# _consonet = []
# for name in names :
#     if name[0]not in "aeiou":
#         _consonet.append(name)
# print(_consonet)
#
# _name_consonent = [name for name in names if name[0] not in "aeiou"]
# _consonet = list(_name_consonent)
# print(_consonet)


# names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']
# _name_greater__=[]
# for name in names:
#     if len(name)>= 5:
#         _name_greater__.append((name,len(name)))
# print(_name_greater__)

# _greater_len=[(name,len(name)) for name in names if len(name)>=5]
# _list = list(_greater_len)
# print(_list)


# # different ways of getting index and item
# # for item in enumerate(numbers):     # item is a tuple
# #     index, name = item      # tuple unpacking
#
# # for item in enumerate(numbers):
# #     index = item[0] # tuple indexing
# #     name = item[1]


# Raise to the power of list index
# numbers = [1, 2, 3, 4, 5]
# index_item = []
# for index, item in enumerate(numbers):
#     index_item.append(item**index)
# print(index_item)


# index_item = [item**index for index, item in enumerate(numbers)]
# _list=list(index_item)
# print(_list)


# import math
# # using comprehension
# numbers = [1, 2, 3, 4, 5]
# __fact = [math.factorial(number) for number in numbers]
# _list = list(__fact)
# print(_list)


# List comprehension to sum the factorial of numbers from 1-5
# numbers = [1, 2, 3, 4, 5]
# _sum = sum([math.factorial(number) for number in numbers])
# # _list = list(_sum)
# print(_sum)


# Build a list of tuples with string and its length pair

# names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']
# str_len_pair = [(name, len(name)) for name in names]
# _list = list(str_len_pair)
# print(_list)


# # Build a list with only even with even length string

# names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']
# even_string = [name for name in names if len(name) % 2 == 0]
# _list = list(even_string)
# print(_list)


# Generating List of PI values
# pi_list = [round(math.pi, n) for n in range(1, 6)]
# _list = list(pi_list)
# print(_list)

# Reverse the item of a list if the item is of odd length string

# names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']
# store = []
# for name in names:
#     if len(name) % 2 != 0:
#         store.append(name[::-1])
# print(store)
# _reverse = [name[::-1] for name in names if len(name) % 2 != 0]
# _list = list(_reverse)
# print(_list)


# Using "else" in Comprehension
# Reverse the item of a list if the item is of odd length string otherwise keep the item as it is.
# names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']

# store = []
# for name in names:
#     if len(name) % 2 != 0:
#         store.append(name[::-1])
#     else:
#         store.append(name)
# print(store)

# _reverse = [name[::-1] if len(name) % 2 != 0 else name for name in names]
# _list = list(_reverse)
# print(_list)
# names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']
# def _reverse(name):
#     if len(name) % 2 == 0:
#         return name
#     else:
#         return name[::-1]
# # # print(_reverse(names))

# _reverse = [_reverse(name) for name in names ]
# _list = list(_reverse)
# print(_list)


# reverse only those items which are of type str
# data = ['hello', 123, 1.2, 'world', True, 'python']
# store = []
# for item in data:
#     if type(item) == str:
#         store.append(item[::-1])
#     else:
#         store.append(item)
# print(store)
#
# _type_rev_str = [item[::-1] if type(item) == str else item for item in data ]
# _list = list(_type_rev_str)
# print(_list)

# def _str_rev(item):
#     if isinstance(item,str):
#         return item[::-1]
#     return item
# print(_str_rev(data))

# _str_rev_item = [_str_rev(item) for item in data]
# _list = list(_str_rev_item)
# print(_list)

# # Building a list of prime numbers from 1-50.

# without using comprehension
# prime_numbers = [ ]
# for i in range(1, 51):
#     if is_prime(i):     # if is_prime(i) == True
#         prime_numbers.append(i)

# def is_prime(number):
#     for i in range(2, number):
#         if number % i == 0:
#             return False
#     return True
# #
# prime_numbers = [ i  for i in range(2, 51) if is_prime(i)]
# li_st = list(prime_numbers)
# print(li_st)

# a = [1, 2, 3, 4]
# b = [5, 6, 7, 8]
# # total = [6, 8, 10, 12]
# total = [ ]
# # for item in zip(a, b):
# #     first_number, second_number = item      # tuple unpacking
# #     total.append(first_number + second_number)
# #
# # # standard practice
# for first_number, second_number in zip(a, b):
#     total.append(first_number + second_number)
#
# _add = [fnumber + snumber for fnumber,snumber in zip(a,b) ]
# _added = list(_add)
# print(_added)


# Multiple "for" loops in comprehension
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# # # o/p [1, 2, 3, 4, 5, 6, 7, 8, 9]
# store= []
# for item in matrix :
#     for _item_initem in item:
#         store.append(_item_initem)
# print(store)
#
# _nested_loops = [number for item in matrix for number in item]
# _nested_loops_in_list= list(_nested_loops)
# print(_nested_loops_in_list)
#
# # # alternate solution
# # for item in matrix:
# #     flat_list.extend(item)

# Concatenating numbers and letters
# letters = "ABCDEFGH"
# numbers = [0, 1, 2, 3, 4, 5, 6, 7]
# def _concat(_letter,_number):
#     return f'{_letter}{_number}'
#
# print(_concat(letters,numbers))

# store= []
# for item,num in zip(letters,numbers):
#     store.append(item+str(num))
# print(store)

# _pair=[item+str(num) for item,num in zip(letters,numbers)]
# _list=list(_pair)
# print(_list)


# # Comprehension with 2 for loops!
# n = [(x, y) for x in range(5) for y in range(5)]
# num=list(n)
# print(num)
#
# countries = {"India": ["Bangalore", "Chennai", "Delhi", "Kolkata"],
#              "USA": ["Dallas", "New York", "Chicago"],
#              "China": ["Bejing", "Shaingai"]
#              }
#
# # Get the list of Country and City in a tuple
# # [("India", "Bangalore"),("India", "Chennai"),("India", "Delhi"),
# # ("India", "Kolkata"),("USA", "Dallas"), ("USA", "New York"),
# # ("USA", "Chicago"), ("China", "Bejing"), ("China", "Shaingai")]
#
# # l = [(country, city) for country, cities in countries.items() for city in cities]
# _city_country = [(country,city) for country,cities in countries.items() for city in cities ]
# print(_city_country)


