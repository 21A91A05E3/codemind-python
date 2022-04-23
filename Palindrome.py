n=int(input())
t=n
r=0
while n:
    d=n%10
    r=(r*10)+d
    n=n//10
if(r==t):
    print("True")
else:
    print("False")