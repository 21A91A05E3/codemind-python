m,n=map(int,input().split())
s=0
l=[list(map(int,input().split()))
for i in range(m)]
for i in range(m):
    for j in range(n):
        if i==j or i+j==m-1:
            s=s+l[i][j]
print(s)