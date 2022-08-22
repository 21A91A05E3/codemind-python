s=input()
l=[]
c=0
c1=0
for i in s:
    l.append(s.count(i))
ma=max(l)
mi=min(l)
for i in s:
    if s.count(i)==ma:
        c1+=1
    elif s.count(i)==mi:
        c+=1
if c1==len(s)-1 or c==len(s)-1 or c1==len(s) or c==len(s):
    print("Valid String")
else:
    print("Not Valid")