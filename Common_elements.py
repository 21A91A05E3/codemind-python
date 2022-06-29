m,n=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
r=[]
for i in l1:
    if i  in l2:
        if i not in r:
            r.append(i)
print(*r)