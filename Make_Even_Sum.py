n=int(input())
l=list(map(int,input().split()))
o=0
e=0
for i in l:
    if i%2:
        o+=1
    else:
        e+=1
if e==n:
    print("1")
elif o%2==0:
    print("1")
else:
    print("0")
    