m,n=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
r=[]
for i in l1:
    if i not in l2:
        r.append(i)
for i in l2:
    if i not in l1:
        r.append(i)
print(*r)