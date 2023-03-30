#d1={} means Set
d2=dict() #To create empty dictionary

fruits={"Apple":"It's a red fruit","Mango":"King of all fruits","Orange":"It's a yellow fruit"}
print(fruits)
print(len(fruits))
# print(fruits[0])  KeyError: 0

#we can't access using index value.
#But we can fetch by using index.
print(fruits["Mango"])
print(fruits["Apple"])

#add more element in dictionary
fruits["leechi"]="Green color fruit"
print(fruits)

print(fruits.keys())# Returns List inside tuple
print(fruits.values())# Returns List inside tuple
print(fruits.items())# Returns List inside tuple

#Add one dictionary into another dictionary

veg={"Tomato":"It's a red veg","potato":"Good for health"}
print(veg)
print(type(veg))
fruits.update(veg)
print(fruits)


#Delete an element from dictionary
del fruits["Mango"]# We can use it on dictionary and List ,We can't use it on tuple and set
print(fruits)



