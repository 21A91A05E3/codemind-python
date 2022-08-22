s=input()
l=[]
for i in s:
    l.append(s.count(i))
m=max(l)
r=[]
for i in s:
    if s.count(i)!=m:
        r.append(i)
if len(r)==0:
    print("-1")
else:
    p=[]
    for i in r:
        p.append(s.count(i))
    ma=max(p)
    for i in r:
        if r.count(i)==ma:
            print(i)
            break

            