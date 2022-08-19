s=input()
r=[]
c=0
for i in s:
    if i.isdigit():
        if i not in r:
            r.append(i)
for i in r:
    if int(i)%2==0:
        c+=1
if c==0:
    print("-1")
else:
    r=sorted(r)
    r=r[::-1]
    for i in range(len(r)):
        if int(r[i])%2==0:
            e=r[i]
    for i in r:
        if i!=e:
            print(i,end="")
    print(e)
        
