m,n=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l1=set(l1)
l2=set(l2)
c=0
for i in l1:
    if i in l2:
        c+=1
print(c)