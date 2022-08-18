n=int(input())
l=list(map(int,input().split()))
e=[]
o=[]
for i in l:
    if i%2==0:
        e.append(i)
    else:
        o.append(i)
i,j=0,0
l1=[]
while(i<len(e) and j<len(o)):
    l1.append(o[j])
    j+=1
    l1.append(e[i])
    i+=1
while(j<len(o)):
    l1.append(o[j])
    j+=1
while(i<len(e)):
    l1.append(e[i])
    i+=1
if len(l1)%2!=0:
    l1.append("0")
print(*l1)