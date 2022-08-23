s=input()
w=s.split()
r=[]
for i in w:
    v=""
    c=""
    l=""
    for j in i:
        if j in "aeiouAEIOU":
            v=v+j
        elif j!=" ":
            c=c+j
    c=sorted(c)
    k=0
    p=0
    for j in i:
        if j in "aeiouAEIOU":
            l=l+v[k]
            k+=1
        elif j!=" ":
            l=l+c[p]
            p+=1
    r.append(l)
for i in r:
    print(i,end=" ")