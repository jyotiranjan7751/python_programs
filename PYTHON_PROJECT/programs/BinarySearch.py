l1=[11,22,33,44,55,66,77,88,99]
key=int(input("enter your choice need to search: "))
start=0
end= len(l1)-1
count=0
while(start<=end):
    mid=(start+end)//2
    if(key==l1[mid]):
        count=1;
        print(f"element is found at index {mid}")
        break;
    elif(key>l1[mid]):
        start=mid+1
    else:
        end= mid - 1
if count==0:
    print("The element is not present")