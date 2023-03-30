def evenOrOdd(num):
    if num%2==0:
        return num
l=[1,2,3,4,5,6,7,8,9,10]
print(list(filter(evenOrOdd,l)))
#It will print all the odd number present in the given list l(Return type is List of odd numbers)