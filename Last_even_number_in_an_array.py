n=int(input())
l=list(map(int,input().split()))
l1=l[::-1]
for i in l1:
    if i%2==0:
        print(i)
        break