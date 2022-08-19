s=input()
c=0
m=0
for i in s:
    if i in "aeiou":
        c+=1
    else:
        m=max(c,m)
        c=0
m=max(c,m)
print(m)