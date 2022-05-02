s=input()
v=0
c=0
d=0
w=0
for i in range(0,len(s)):
    ch=s[i]
    if((ch>='a' and ch<='z') or (ch>='A' and ch<='Z')):
        ch=ch.lower()
        if(ch=='a'or ch=='e'or ch=='i'or ch=='o'or ch=='u'):
            v+=1
        else:
            c+=1
    elif(ch>='0' and ch<='9'):
        d+=1
    else:
        w+=1
print('Vowels:',v)
print('Consonants:',c)
print('Digits:',d)
print('White spaces:',w)
