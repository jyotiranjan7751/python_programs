def square(num):
     return num*num
# l=[2,5,3,7,8]
# print([map(square,l)])
#o/p=[<map object at 0x000001B7106D6740>] wrong o/p below code is correct


l=[2,5,3,7,8]
print(list(map(square,l)))
#It will print square of each element present in the List=l(Return type is List)