for i in range(1,11):
    print(i,end=" ,")
    
print()

for i in range(10,0,-1):
    print(i,end=" ,")
print()

def test(j):
    return True
b=test(2)

if b:
    print("true")
    
for i in range(1,11):
    print(i,end=" ,")
    b=test(i)