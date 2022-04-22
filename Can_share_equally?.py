a,b=map(int,input().split())
m=a%2
n=b%2
if (m==0 and (a>0 or n==0)):
    print('YES')
else :
    print('NO')
