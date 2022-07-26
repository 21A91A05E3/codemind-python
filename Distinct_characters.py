s=input()
s=s.lower()
l=[]
for i in s:
    if s.count(i)==1:
        if i!=" ":
            l.append(i)
l=sorted(l)
print("".join(l))
