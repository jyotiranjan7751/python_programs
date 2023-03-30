for i in range(1,11):
    print(i)
    if i==5:
        break

print("="*50)

for i in range(1,11):
    if i==5:
        continue
    print(i)

print("="*50)
    
for i in range(1,11):
    if (i>=4 and i<=7):
        continue
    print(i)
