n=int(input())
l=list(map(int,input().split()))
m=min(l)
for i in range(len(l)):
    s=0
    for j in range(i,len(l)):
        s+=l[j]
        m=max(m,s)
print(m)