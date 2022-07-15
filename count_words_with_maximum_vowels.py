s=input()
w=s.split()
m=0
vc=0
for i in w:
    c=0
    for j in i:
        if j in 'aeiouAEIOU':
            c+=1
    if(c>=m):
        m=c
for i in w:
    c=0
    for j in i:
        if j in 'aeiouAEIOU':
            c+=1
    if(c==m):
       vc+=1
print(vc)