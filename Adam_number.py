n=int(input())
s1=n*n
r=0
while n>0:
    d=n%10
    r=(r*10)+d
    n=n//10
s2=r*r
r1=0
while s2>0:
    d=s2%10
    r1=(r1*10)+d
    s2=s2//10
if(r1==s1):
    print("True")
else:
    print("False")
    
