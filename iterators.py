
# Iterable - __iter__ () or __getitem__()
# Iterator - __next__()
#Iteration - it detects the given data is iterable or not ,if it is iterable then it goes to iterable

# Iterable runs and gives __iter__() function
# __iter__() function generates  iterator
# and iterator gives the next values by running the __next__() function


# nums = [7,8,9,12,45,]
# for number in nums:
#     print(number)


# nums = [7,8,9,12,45,]
# for number in nums:
#     print(number)


# nums = [7,8,9,12,45,]
# it = iter(nums)
# print(it.__next__())
# print(it.__next__())
# print(next(it))


# class Top_ten:
#     def __init__(self):
#         self.num = 1
#
#     def __iter__( self ):
#         return self
#
#     def __next__( self ):
#         if self.num<=10:
#             value = self.num
#             self.num += 1
#             return value
#         else:
#             raise StopIteration


# value = Top_ten ( )
# print ( next(value) )
# print ( value.__next__() )
# for number in value:
#     print(number)