s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
r=""
for i in s1:
    if i!=" ":
        if i not in s2:
            if i not in r:
                r=r+i
for i in s2:
    if i!=" ":
        if i not in s1:
            if i not in r:
                r=r+i
if len(r):
    print("".join(sorted(r)))
else:
    print("-1")