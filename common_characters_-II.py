s1=input()
s2=input()
if len(s1)<len(s2):
    s1=s1.lower()
else:
    s2=s2.lower()
r=""
c=0
for i in s1:
    if i!=" ":
        if i in s2:
            if i not in r:
                r=r+i
                c+=1
print(c)