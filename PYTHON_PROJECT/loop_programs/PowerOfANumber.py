num=int(input("enter a number"))
power=int(input("enter the power"))
result=1
for i in range(1,power+1):
    result*=num;
    
print(result)
#OR
print(num**power)