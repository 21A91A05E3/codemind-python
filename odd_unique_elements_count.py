n=int(input())
l=list(map(int,input().split()))
r=set(l)
c=0
for i in r:
    if(i%2==1):
        c+=1
print(c)