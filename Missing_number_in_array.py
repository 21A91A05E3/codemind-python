t=int(input())
while(t):
    n=int(input())
    sum=0
    os=(n*(n+1))//2
    a=list(map(int,input().split()))
    for i in a:
        sum=sum+i
    print(os-sum)
    t-=1
