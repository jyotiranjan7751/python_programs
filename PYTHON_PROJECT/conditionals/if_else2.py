username=input("Please enter the username")
if(username=='jyoti'):
    password=input("hello "+username+" please enter your password.")
    if password=="1234":
        print("Access granted to- "+username)
    else:
        print("password didn't match")
else:
    print("username is incorrect")
