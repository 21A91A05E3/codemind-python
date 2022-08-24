t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    r=[]
    c=0
    for j in range(n):
        for k in range(j+1,n):
            if j!=k:
                r.append(l[j]+l[k])
    for p in r:
        if p in l:
            c+=1
    if c:
        print(c)
    else:
        print("-1")
            