a,b=map(int,input().split())
l=list(map(int,input().split()))
r=list(map(int,input().split()))
for j in r:
    if j in l:
        x=l.index(j)
        l[x]=-1
    else:
        print("No")
        break
else:
    print("Yes")
        