#Print the 1st 10 multiple of 3 from 1 to 50
count=0
for i in range(3,50):
   if(i%3==0):
       print(i)
       count+=1
       if (count==10):
           break