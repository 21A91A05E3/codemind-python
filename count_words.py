s=input()
w=s.split()
c=0
for word in w:
    if word[0] in 'AEIOUaeiou':
        if word[-1] not in 'AEIOUaeiou':
            c+=1
print(c)