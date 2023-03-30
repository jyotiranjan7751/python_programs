
class Student:
    def __init__(self,name,address,course):
        self.name=name
        self.address=address
        self.course=course
        print(f"Student details {self.name}, {self.address} and {self.course}")
s1=Student("Sheela","Bangalore","Software Testing")
print(s1.name)
print(s1.address)
print(s1.course)
print(s1)
s1.name="dinga"
print(s1.name)
s2=Student("Malla","Hydrabad","Software QA")


#hasattr(),getattr(),setatt(),delattr()
print(hasattr(s1, "name"))#True because name is there
print(getattr(s1, "name"))
print(hasattr(s1, "phone"))
setattr(s1, "phone", "12345")
print(hasattr(s1, "phone"))
delattr(s1,"phone" )
print(hasattr(s1, "phone"))

















# class Test:
#     name="dinga"
#
# t=Test()
# print(t.name)
# t1=Test()
# print(t1.name)
# t1.name="Changed"
# print(t.name)
# print(t1.name)
# Test.name="ChangedDemo"
# print()
# print(t.name)
# print(t1.name)tr(sphone")



