n=int(input())
l=list(map(int,input().split()))
e=0
for i in l:
    if i%2==0:
        e=e+i
print(e)