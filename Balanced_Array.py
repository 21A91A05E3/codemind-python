def ba(arr, n):
    for i in range(0, n):
        ls=sum(arr[0:i])
        rs=sum(arr[i+1:])
        if(ls==rs):
            return 1
    return 0
t=int(input())
for i in range(t):
    n = int(input())
    l=list(map(int,input().split()))
    if(ba(l,n)):
        print("YES")
    else:
        print("NO")
    
    
