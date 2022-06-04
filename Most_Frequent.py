n=int(input())
l=list(map(int,input().split()))
c=0
m=0
for i in l:
    c=l.count(i)
    if c>m:
        m=c
        e=i
    if(c==m and i<e):
        e=i
print(e)
        