n=int(input())
l=list(map(int,input().split()))
n1=int(input())
l1=list(map(int,input().split()))
k=int(input())
c=0
for i in range(n):
    if(l[i]<k and l1[i]<k):
        continue
    elif(l[i]>k):
        continue
    else:
        c+=1
print(c)