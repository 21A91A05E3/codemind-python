n=int(input())
l=list(map(int,input().split()))
k=int(input())
for i in range(len(l)):
    print(l[(n-k+i)%n],end=" ")
