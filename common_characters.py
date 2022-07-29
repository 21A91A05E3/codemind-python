s1=input()
s2=input()
if len(s1)<len(s2):
    s1=s1.lower()
else:
    s2=s2.lower()
r=""
for i in s1:
    if i!=" ":
        if i in s2:
            if i not in r:
                r=r+i
if len(r):
    print("".join(sorted(r)))
else:
    print("-1")