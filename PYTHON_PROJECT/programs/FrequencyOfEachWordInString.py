freq={}
s1="jyotiranjan nath from odisha"
s2=s1.split(" ")
for i in s2:
    if i not in freq:
        freq[i]=1
    else:
        
        freq[i]=freq[i]+1;
print(freq)   

# s3=" ".join(s2)
# print(s3)