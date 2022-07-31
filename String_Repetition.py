s=input()
n=int(input())
c=s.count('a')
t=n
t=t//len(s)
t=t*c
n=n%len(s)
for i in range(0,n):
    if s[i]=='a':
        t+=1
print(t)