n=int(input())
l=list(map(int,input().split()))
k=int(input())
m=max(l)
for i in l:
    if i+k>=m:
        print("True",end=" ")
    else:
        print("False",end=" ")