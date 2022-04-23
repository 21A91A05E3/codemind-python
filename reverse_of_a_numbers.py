n=int(input())
r=0
while n:
    d=n%10
    r=(r*10)+d
    n=n//10
print(r)