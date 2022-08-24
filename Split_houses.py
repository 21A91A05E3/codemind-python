n=int(input())
s=input()
r=""
c=0
for i in s:
    if i=='.':
        r=r+'B'
    else:
        r=r+i
for i in range(0,len(r)-1):
    if r[i]==r[i+1]=='H':
        c+=1
if c!=0:
    print("NO")
else:
    print("YES")
    print(r)
    