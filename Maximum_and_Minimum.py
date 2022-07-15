n=int(input())
l=list(map(int,input().split()))
r=[]
for i in l:
    if(l.count(i)==i):
        r.append(i)
if(len(r)):
    print(min(r),end=" ")
    print(max(r))
else:
    print("-1")