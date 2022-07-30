s=input()
w=s.split()
c=0
for i in w:
    f=i[0]
    l=i[-1]
    if f in 'AEIOUaeiou':
        if l not in 'AEIOUaeiou':
            c+=1
print(c)