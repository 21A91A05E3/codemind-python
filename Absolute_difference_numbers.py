n,d=map(int,input().split())
l=[]
while(n):
    r=n%10
    l.append(r)
    n=n//10
z=l[::-1]
s=0
e=0
i=0
j=d-1
while(d):
    s+=z[i]*pow(10,d-1)
    e+=l[j]*pow(10,d-1)
    i+=1
    j-=1
    d-=1
print(abs(s-e))