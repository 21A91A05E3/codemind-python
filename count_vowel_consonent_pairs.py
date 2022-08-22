s=input()
c=0
r=s[::-1]
for i in range(len(s)//2):
    if s[i] in 'aeiouAEIOU':
        if r[i] not in 'aeiouAEIOU':
            if r[i]!=" ":
                c+=1
    elif s[i] not in 'aeiouAEIOU':
        if r[i] in 'aeiouAEIOU':
            if s[i]!=" ":
                c+=1
print(c)
    
        