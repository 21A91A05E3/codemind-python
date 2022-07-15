n=int(input())
l=list(map(int,input().split()))
r=[]
for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        d=l[j]-l[i]
        r.append(d)
m=max(r)
if(m>0):
    print(m)
else:
    print("0")
    