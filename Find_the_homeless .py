n=int(input())
p=[]
h=[]
c=0
for i in range(2*n):
    k=int(input())
    if c<n:
        c+=1
        p.append(k)
    else:
        h.append(k)
p=sorted(p)
h=sorted(h)
d=0
for i in range(n):
    if p[i]<=h[i]:
        d+=1
print(n-d)

    