t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    l=l1+l2
    l=sorted(l)
    print(*l)
    