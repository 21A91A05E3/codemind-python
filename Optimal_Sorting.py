t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    s=sorted(l)
    if l==s:
        print("0")
    else:
        print(max(l)-min(l))