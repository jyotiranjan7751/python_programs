s1=[10,2.34,"jyoti",None,10,'a']
print(s1)
print(s1[2])
print(s1[-1])

s1[5]='x'
print(s1)

print(len(s1))

print(s1[:])
print(s1[0:])
print(s1[2:5])


#In operator in List
print(55  in s1)#False
print(10 in s1)#True
print(10 not in s1)#False

#s1.clear()
#print(s1)

s2=[]#empty list
s3=list()#empty list
s2=s1.copy()
print(s2)


print("="*100)

s1=[11,22,33,44,55,66,77,88,9,111]
print(s1)
s1.append(222)#It will add the value in the last index
print(s1)
s1.pop()#it will remove the last element in the list
print(s1)

s1.remove(55)#It will remove 55 from the list
print(s1)

s1.insert(5,1000)
print(s1)#It will add "1000" in the 5th index

s1.reverse()#It will reverse the list
print(s1)

s1.sort()
print(s1)#It will sort the List


