num=int(input("Enter the number"))
for i in range(1,11):
    print(str(num)+" * "+str(i)+" = "+str(num*i))
    
print("Printing in reverse using range function")

for i in range(10,0,-1):
    print(i)
    
print("Skipping numbers in between using range() function")

for i in range(1,20,2):
    print(i,end=" ")

print()
print("="*100)
    
for i in range(7,101,7):
    print(i,end=" ")
    
print()
print("="*100)

for i in range(101,7,-7):
    print(i,end=" ")