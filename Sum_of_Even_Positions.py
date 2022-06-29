n=int(input())
l=list(map(int,input().split()))
e=0
for i in range(0,len(l)):
    if i%2==0:
        e=e+l[i]
print(e)