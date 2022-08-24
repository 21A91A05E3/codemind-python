n=int(input())
l=list(map(int,input().split()))
r=[]
for i in range(len(l)):
    m=-1
    for j in range(i+1,len(l)):
        if l[j]>m:
            m=l[j]
    r.append(m)
print(*r)