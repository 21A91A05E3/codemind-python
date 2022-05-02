s=input()
cz=0
co=0
for i in range(0,len(s)):
    ch=s[i]
    if(ch=='z'):
        cz+=1
    else:
        co+=1
if(co==2*cz):
    print("Yes")
else:
    print("No")
