s=input()
r=""
for i in s:
    if i in 'AEIOUaeiou':
        if i not in r:
            r=r+i
for j in r:
    print(j,end=" ")
        