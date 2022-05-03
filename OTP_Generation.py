n=int(input())
r=0
while n:
    d=n%10
    r=r*10+d
    n=n//10
while r:
    d=r%10
    if(r%2!=0):
        print(d*d,end='')
    r=r//10
