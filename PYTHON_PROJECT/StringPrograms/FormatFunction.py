a=10
b=20
print("The sum of {} and {} is {}".format(a,b,(a+b)))


a=10
b=20
print("The sum of {0} and {1} is {2}".format(a,b,(a+b)))


a=10
b=20
print("The sum of {1} and {0} is {2}".format(a,b,(a+b)))


for i in range(1,11):
    print("{} squre={}, qube={}".format(i,i*i,i*i*i))
    
    
for i in range(10000,999,-1000):
    print(" {}'s 10%={}, 20%={}, 30%={} ".format(i,(10/100)*i,(20/100)*i, (30/100)*i))