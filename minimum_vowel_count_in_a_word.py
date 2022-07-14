s=input()
w=s.split()
m=100
for i in w:
    c=0
    for j in i:
        if j in 'aeiouAEIOU':
            c+=1
    if(c<=m):
        m=c
print(m)