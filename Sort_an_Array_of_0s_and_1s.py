n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    if i==0:
        c+=1
for i in range(len(l)):
    if i<c:
        print("0",end=" ")
    else:
        print("1",end=" ")

    