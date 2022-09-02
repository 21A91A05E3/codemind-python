n=int(input())
a=[list(map(int,input().split()))
for i in range(n)]
p=0
s=0
for i in range(n):
    for j in range(n):
        if(i==j):
            p=p+a[i][j]
        if(i==n-j-1):
            s=s+a[i][j]
print("Principal Diagonal",end="")
print(":",end="")
print(p)
print("Secondary Diagonal",end="")
print(":",end="")
print(s)