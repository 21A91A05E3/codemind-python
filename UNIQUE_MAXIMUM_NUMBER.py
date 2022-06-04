n=int(input())
l=list(map(int,input().split()))
e=0
c=0
for i in l:
    if l.count(i)==1:
        if i>e:
            c+=1
            e=i
if c==0:
    print("-1")
else:
    print(e)