import math
x,y,m=map(int,input().split())
p=math.pow(x,y)
r=p%m
print(int(r))