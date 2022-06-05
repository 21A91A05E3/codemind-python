s=input()
s=s.lower()
w=s.split()
c=0
for i in w:
    if(i==i[::-1]):
        c+=1
print(c)