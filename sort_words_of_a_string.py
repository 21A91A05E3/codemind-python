s=input()
w=s.split()
r=[]
for i in w:
    v=""
    c=""
    l=""
    for j in i:
        if j.isalpha():
            v=v+j
        else:
            c=c+j
    v=sorted(v)
    k=0
    p=0
    for j in i:
        if j.isalpha():
            l=l+v[k]
            k+=1
        else:
            l=l+c[p]
            p+=1
    r.append(l)
for i in r:
    print(i,end=" ")