# import keyword
# print(keyword.kwlist)

# print(dir(__builtins__))#It will print all in-built functions

# print(dir(str))#It will print all in-builts in String


s1="ecodeRs"
print(s1.capitalize())#It wii captilize only 1st character
print(s1.casefold())#It will convert Upper Case to lower case
print(s1.swapcase())#It will convert upper case to lower case and lower case to upper case

print(s1.upper())#It will convert all to upper case
print(s1.lower())#It will conver all to lower case

print(s1.isupper())#Check the string in upper case or not return type is boolean
print(s1.islower())##Check the string in lower case or not return type is boolean

print(len(s1))#it will gives the size of the string

print(s1.count("e"))#It wiil gives the count of "e" in the given string

print(s1.startswith("e"))#true
print(s1.endswith("s"))#true

print(s1.find("d",))#3
print(s1.index("d"))#3
print(s1.rindex("e"))#4

print(s1.isalpha())#True --->Is it contains only alphabet 
print(s1.isalnum())#True---> Is it a alpha-Numeric 
print(s1.isnumeric())#False--->Is it contains only Numeric 
print(s1.isdigit())#False
print(s1.isspace())#False


s1="This Is A Nice Class"
print(s1.istitle())#True if each words in upper case

userName="     jyoti....."
print(userName)
print(userName.lstrip(" ").rstrip("."))

userName="jyoti"
print(userName.ljust(20, "_"))
print(userName.rjust(20, "0"))


s1="Hello welcome to skillmine"
print(len(s1))
s2=s1.split(" ")#It will split when there is a space  and return  in List
print(s2)
print(len(s2))








