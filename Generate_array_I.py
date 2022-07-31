n=int(input())
l=list(map(int,input().split()))
for i in range(0,len(l),2):
    j=l[i+1]
    while(j):
        print(l[i],end=" ")
        j=j-1