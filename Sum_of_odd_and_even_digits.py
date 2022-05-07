n=int(input())
e=0
o=0
ls=list(map(int,input().split()))
for i in range(0,len(ls)):
    if(i%2==0):
        e=e+ls[i]
    else:
        o=o+ls[i]
if(e-o==0):
    print("YES")
else:
    print("NO")