
username=input("Enter your name")#It will takes only String inputs from user
print("Hello "+username)

age=int(input("enter your age"))
#print(age)
#print("you have entered age as: "+age)-->Here we can not concate string and int like java
print("you have entered age as: "+str(age))#To concate String and int we r using str()

price=float(input("Give the price of the book in decimal number"))#Here user can't enter Strring value
print("The price entered is: "+str(price))

