s1={11,11,22,22,33,44,55,55}
s2={55,55,66,66,77,88,99}
print(s1.union(s2))
print(s1.intersection(s2))

s1.update(s2)
print(s1)
print(s2)

s2.update(s1)
print(s2)
print(s1)
