n=int(input())
l=list(map(int,input().split()))
s=0
c=0
for i in l:
    s=s+i
r=s//n
for j in l:
    if j<=r:
        c+=1
print(c)
