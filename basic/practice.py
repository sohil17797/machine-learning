# print(round(3.4))
# print(abs(3.4))

# list unpacking

# a,b,c, *other, d = [1,2,3,4,5,6,7,8,9,10]

# print(a)
# print(b)
# print(c)
# print(other)
# print(d)

# print(None)
# user = {
# 'basket': [1,2,3],
# 'greet': 'hello'}

# print(user.get('age'))  

# while True:
#     responce = input("hello hi! ")
    
#     if responce == 'bye':
#         break

# def super_func(*args, **kwargs):
#     total = 0
#     for items in kwargs.values():
#         total +=items
#     return sum(args) + total

# print( super_func(1,2,3,4,5, num1=5 ,num2=10))

# def highest_even(list1):
#     even = []
#     for value in list1:
#         if value % 2 ==0:
#             even.append(value)
#     return max(even)
        

# print(highest_even([1,2,3,4,5,6,7]))

# total = 0
# def count():
#     global total   
#     total += 1
#     return total

# count()
# count()
# print (count())

# def outer():
#     x = 'Local'
#     def inner():
#         nonlocal x
#         x = 'nonlocal'
#         print('inner' ,x)
        
#     inner()
#     print("outer ",x)
    
# # outer()

# def multiplyby_2(item1):
#     return item1*2

# print(list(map(multiplyby_2,[1,2,3,4,5])))

# l1 = [1,2,3,4,5,6]

# def odd(value):
#     return value % 2 !=0 

# print(l1)
# print(list(filter(odd,l1)))

# my_l1 = [1,2,3]
# you_l2 = [4,5,6]

# print(list(zip(my_l1, you_l2)))

from functools import reduce
