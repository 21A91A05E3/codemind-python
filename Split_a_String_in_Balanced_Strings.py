s=input()
d={'R':0,'L':0}
c=0
for i in s:
    d[i]+=1
    if(d['R']==d['L']):
        c+=1
        d['R']=0
        d['L']=0
print(c)