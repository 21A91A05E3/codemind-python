n=int(input())
l=list(map(int,input().split()))
c=0
m=0
for i in l:
    if(i):
        c+=1
    else:
        if(c>m):
            m=c
        c=0
if(c>m):
    m=c
print(m)