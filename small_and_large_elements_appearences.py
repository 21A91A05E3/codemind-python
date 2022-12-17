s=input()
r=""
for i in s:
    if i.isalpha():
        r+=i
l=min(r)
m=max(r)
print(l,end=" ")
print(s.count(l),end=" ")
print(m,end=" ")
print(s.count(m))