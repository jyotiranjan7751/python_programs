# username=input("Please enter the user name...\n")
# if username.find(" ")==-1 and username.isalpha() and username.isnumeric():
#      password=input("Please enter the password")
#      if password.isnumeric() and username.find(" ")==-1:
#          print("Welcome to the HomePage")
# else:
#     print("Invalid username")





# s="7"
# print(s.is)

for i in range(0,5):
    for j in range(0,5):
        if i%2==0:
            if j%2==0:
                print("1",end=" ")
            else:
                print("0",end=" ")
        else:
            print("0",end=" ")
    print()


