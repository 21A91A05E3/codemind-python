n=int(input())
while(n):
    r=-1
    a,b=map(int,input().split())
    for j in range(0,b):
        if((j*j)%b==a):
            r=j
            break
    print(r)
    n-=1
