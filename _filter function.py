# def _even(item):
#     if item % 2 == 0:
#         return item
#
# f = filter(_even,range(1,10))
# print(list(f))
#--------------------------------------------------------------------------------------------------------
# # Build a list with only even with even length string using filter func
# names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']
# # Returns the string if the string has even number of characters.
# def _even_evenlen(item):
#     if len(item) % 2 ==0:
#         return item
# f = filter(_even_evenlen,names)
# print(list(f))

# names = ['laura', 'steve', 'bill', 'james', 'bob', 'greig', 'scott', 'alex', 'ive']
# # # Returns the string if the string is starting from vowel character
# def _vowels(item):
#     if item[0] in "aeiou":
#         return item
# _string = filter(_vowels,names)
# print(list(_string))


# Get only those lines which has TRACE.
# def logmesseges(line):
#     if 'TRACE' in line :
#         return line
# _logfile_open = open('sample.log')
# _trace = filter(logmesseges,_logfile_open)
# print(list(_trace))