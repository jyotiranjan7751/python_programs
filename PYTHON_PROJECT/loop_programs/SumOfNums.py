sum=0;
mul=1;
oddSum=0;
evenSum=0;

for i in range(1,11):
    sum+=i
    mul*=i
    if(i%2==0):
        evenSum+=i
    else:
         oddSum+=i
print("Sum: "+str(sum))
print("Multiplication: "+str(mul))
print("Odd sum: "+str(oddSum))
print("Even sum: "+str(evenSum))



