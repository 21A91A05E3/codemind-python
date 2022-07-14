s=input()
c=0
m=0
for i in s:
    if(i in "aeiou"):
        c+=1
    else:
        if(c>m):
            m=c
        c=0
if(c>m):
    m=c
print(m)