n=int(input())
l=list(map(int,input().split()))
r=""
for i in l:
    c=0
    while(i):
        d=i%10
        c+=1
        i=i//10
    r=r+str(c)
m=min(r)
dc=0
for i in r:
    if i==m:
        dc+=1
print(dc)