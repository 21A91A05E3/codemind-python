t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    a=[]
    for j in range(len(l)):
        a.append(l[(n-k+j)%n])
    print(*a)