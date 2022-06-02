s=input()
r=""
for i in s:
    if(i=='.'):
        i='[.]'
    else:
        i=i
    r=r+i
print(r)