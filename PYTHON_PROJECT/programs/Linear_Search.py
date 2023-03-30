l1=[11,22,33,44,55,66,55]
a=5
res=False
for i in l1:
    if a in l1:
        res=True
        break
if res:
    print(a,"is present")
else:
    print(a,"is not present")