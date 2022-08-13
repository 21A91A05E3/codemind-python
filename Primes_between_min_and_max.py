def p(n):
    if n==0 or n==1:
        return 0
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return 0
        else:
            return 1
n=int(input())
l=list(map(int,input().split()))
s=min(l)
si=l.index(s)
b=max(l)
bi=l.index(b)
c=0
if bi<si:
    bi,si=si,bi
for i in range(si,bi+1):
    if(p(l[i])):
        c+=1
print(c)