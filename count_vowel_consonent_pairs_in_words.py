st=input()
w=st.split()
c=0
for i in range(len(w)):
    s=w[i]
    r=s[::-1]
    for i in range(len(s)//2):
        if s[i] in 'aeiouAEIOU':
            if r[i] not in 'aeiouAEIOU':
                c+=1
        elif s[i] not in 'aeiouAEIOU':
            if r[i] in 'aeiouAEIOU':
                c+=1
print(c)

