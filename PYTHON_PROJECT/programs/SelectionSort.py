def findMinIndex(i,l):
    MinIndex=i
    MinValue=l[i]
    for j in range(i+1,len(l)):
        if l[j]<MinValue:
            MinValue=l[j]
            MinIndex=j
    return MinIndex

l1=[11,55,33,22,77,66,1,3,2]
for i in range(0,len(l1)):
    minIndex=findMinIndex(i,l1)
    temp=l1[minIndex]
    l1[minIndex]=l1[i]
    l1[i]=temp
print(l1)