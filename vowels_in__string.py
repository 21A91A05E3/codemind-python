s=input()
r=""
c=0
for i in s:
    c+=1
    if i in "aeiouAEIOU":
        if i not in r:
            r=r+i
            print(i,end=" ")
if c==0:
    print("-1")