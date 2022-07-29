s=input()
s=s.lower()
l=[]
for i in s:
    if i not in l:
        if i!=" ":
            l.append(i)

print(len(l))