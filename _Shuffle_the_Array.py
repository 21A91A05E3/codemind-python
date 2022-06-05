n=int(input())
l=list(map(int,input().split()))
m=n//2
for i in range(m):
    j=i+m
    print(l[i],l[j],end=" ")