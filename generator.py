# def gen ():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
# gen_obj = gen()
# print(gen_obj.__next__())
# print(gen_obj.__next__())
# print(next(gen_obj))
# print(next(gen_obj))
#


# def gen ():
#     print("generator executing")
#     yield 1
#     yield 2
#     yield 3
#     yield 4
# gen_obj = gen()
# print(gen_obj.__next__())
# print(gen_obj.__next__())
# print(next(gen_obj))
# print(next(gen_obj))


# def _func():
#     """generator function"""
#     print("hello")
#     print('how are you')
#     a = 2
#     print(a)
#     yield "hi"      # the control gets paused here
#     print("world")
#     yield "bye"
# print(next(_func()))


# # normal function
# def even ():
#     store = []
#     for item in range(20):
#         if item % 2 ==0:
#             store.append(item)
#     return store
# print(even())


# # generator function (lazy iterables)
# def g_evens():
#     for i in range(21):
#         if i % 2 == 0:
#             yield i
# res=(g_evens())
# print(list(res))
#
# # generator expression
# gen = (item for item in range(0,21) if item % 2== 0)
# print(list(gen))


# def sam():
#     print('hai')
#     yield 1
#     print('hello')
#     yield 2
#     print("shekhar")
# result = sam()
# print(list(result))


# def com(_list):
#     for item in _list:
#         if type(item) == complex:
#             yield item
# result = com([5+4j,15,'jai',55])
# print(list(result))


# to  generate first n natural number
# def firstn(num):
#     n = 1
#     while n <=num:
#         yield n
#         n = n + 1
# for item in firstn(10):
#     print(item)


#to generate fibonacci number
# def fibb():
#     a,b=0,1
#     while True:
#         yield a
#         a,b=b,a+b
# for num in fibb():
#     if num >100:
#         break
#     print(num)


# names = ['laura', 'steve', 'bill', 'james', 'bob', 'greig', 'scott', 'alex', 'ive']
# def _vowels():
#     for vowel in names:
#         if vowel[0] in 'aeiou':
#             yield vowel
# res = _vowels()
# print(list(res))


# names = ["apple", "google", "yahoo", "gmail", "flipkart", "yelp"]
# # [("apple", 5), ("google", 6), ("yahoo", 5)]
# def item_len_pair():
#     for name in names:
#         yield name,len(name)
# result= item_len_pair()
# print(list(result))


# # using list comprehension
# items = [ (name, len(name))  for name in names ]

#generator expression
# gen = ((name,len(name))for name in names)
# print(list(gen))