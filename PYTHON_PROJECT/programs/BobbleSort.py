l1=[8,7,3,1,2,5,77,66]
for i in range(1,len(l1)):
    for j in range(0,len(l1)-i):
        if l1[j]>l1[j+1]:
            temp=l1[j]
            l1[j]=l1[j+1]
            l1[j+1]=temp
print(l1)
