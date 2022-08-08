a,b=map(int,input().split())
l=list(map(int,input().split()))
s=l[b:]+l[:b]
print(*s)

    