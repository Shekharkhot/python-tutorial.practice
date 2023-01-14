# Building a dict of word and length pair
# words = "This is a bunch of words"
# words= {word:len(word) for word in words.split()}
# _dict = dict(words)
# print(_dict)


# Flipping keys and values of the dictionary using dict comprehension
# d = {'a': 1, 'b': 2, 'c': 3}
# _flip = {value:key for key,value in d.items()}
# _dict = dict(_flip)
# print(_dict)
#
# sentence = "hello world welcome to python hello hi world welcome to python"
# _dict_word_count= {word:sentence.count(word) for word in sentence.split(" ")}
# _dict = dict(_dict_word_count)
# print(_dict)


# Counting the number of each character in a String
# my_string = 'guido van rossum'
# _char_count={ item:my_string.count(item) for item in my_string }
# _dict = dict(_char_count)
# print(_dict)


# Dictionary of character and ascii value pairs
# char = 'abcABC'
# dict_ascii = { item:ord(item) for item in char }
# print(dict_ascii)
# # _dict = dict(dict_ascii)
# # print(_dict)


# Buildings
# buildings = {
#                 'burj khalifa':                     828,
#                 'Shanghai_Tower':                   632,
#                 'Abraj_Al_Bait_Clock Tower':        601,
#                 'Ping_An_Finance_Centre_Shenzhen':  599,
#                 'Lotte World Tower':                554.5,
#                 'World Trade Center':               541.3
#                 }
# buildings_feets={building :height * 3.28 for building,height in buildings.items()}
# print(buildings_feets)


# Creating Dictionary of city and population pairs using Dict Comprehension
# cities = ['Tokyo',
#           'Delhi',
#           'Shanghai',
#           'Sao Paulo',
#           'Mumbai'
#           ]
# population = ['38,001,000',
#               '25,703,168',
#               '23,740,778',
#               '21,066,245',
#               '21,042,538'
#               ]
#
# city_pair = {city:pop for city,pop in zip(cities,population)}
# print(city_pair)

#
# # Dial Codes
# dial_codes = [
#     (86, 'China'),
#     (91, 'India'),
#     (1, 'United States'),
#     (62, 'Indonesia'),
#     (55, 'Brazil'),
#     (92, 'Pakistan'),
#     (880, 'Bangladesh'),
#     (234, 'Nigeria'),
#     (7, 'Russia'),
#     (81, 'Japan')
#     ]
# _dial_code_country = {country : code for code,country in dial_codes}
# print(_dial_code_country)


# Building a dictionary whose price value is more than 200
# prices = {
#     'ACME': 45.23,
#     'AAPL': 612.78,
#     'IBM': 205.55,
#     'HPQ': 37.20,
#     'FB': 10.75 }
# _pricevalue = {company :price for company,price in prices.items() if price >= 200}
# print(_pricevalue)


# Set Comprehension
# The difference between Dictionary Comprehension and Set Comprehension is that the set Comprehension does not
# have key value pair

# find set of square
# nums = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4]
# _set = {num ** 2 for num in nums}
# print(_set)

