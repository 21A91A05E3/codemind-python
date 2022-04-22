import math
a,b,c=map(int,input().split())
s=(a+b+c)/2
r=s*(s-a)*(s-b)*(s-c)
r1=math.sqrt(r)
print('%.2f'%r1)