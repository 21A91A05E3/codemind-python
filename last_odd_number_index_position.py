n=int(input())
l=list(map(int,input().split()))
l1=l[::-1]
for i in range(len(l1)):
    if l1[i]%2==1:
        print(n-i-1)
        break