# import nothing

# print(nothing.devide(2,3))
# print(nothing.multi(2,3))

# import shoping.shoping_cart

# print(shoping.shoping_cart)
import copy
l1 = [[1,2,3],[4,5,6],[7,8,"a"]]
k = copy.copy(l1)
k[2][2]= 9
print(k)
print(l1)