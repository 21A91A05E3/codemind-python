n=int(input())
c=0
l=list(map(int,input().split()))
l=set(l)
for i in l:
    if i%2==1:
        c+=1
print(c)
        