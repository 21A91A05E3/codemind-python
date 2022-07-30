n=int(input())
c=0
for i in range(n):
    s=input()
    for j in range(4):
        if s[j]=='+':
            c+=1
            break
        elif s[j]=='-':
            c-=1
            break
print(c)
        