n1=float(input("Enter the 1st number\n"))
n2=float(input("Enter the 2nd number\n"))
a=int(input("Enter a number---> for addition=1,sub=2 , mul=3, div=4\n"))
if a==1:
    print("addition is: ", n1+n2)
elif a==2:
    print("Substraction is: ", n1 - n2)
elif a==3:
    print("Multiplication: ",n1*n2)
elif a==4:
    print("Division: ",n1/n2)
else:
    print("invalid number, only enter a number from 1 to4 ")