s1={11,11,22,22,33,44,55,55}
s2=set()
print(s1)

# print(s1[0])  TypeError: 'set' object is not subscriptable

s1.add(66)
print(s1)

# del s1(11) cannot delete function call

#In order to delete elements for set we have to functions remove(),discard()

# s1.remove(66)
# print(s1)

# s1.remove(66) KeyError: 66-->It throw error because the 66 is not presenr 

s1.discard(66)
print(s1)
s1.discard(66) # It will not throw an error no matter whether the element is present or not

if 66 in s1:
    s1.remove(66)
else:
    print("66 is not present")