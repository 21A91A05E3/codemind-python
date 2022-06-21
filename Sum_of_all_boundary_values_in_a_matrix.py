m,n=map(int,input().split())
l=[list(map(int,input().split()))for i in range(m)]
s=0
for i in range(m):
    for j in range(n):
        if i==0 or j==0 or i==m-1 or j==n-1:
            s=s+l[i][j]
print(s)