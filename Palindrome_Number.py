t=int(input())
while(t!=0):
    n=int(input())
    r=0
    x=n
    while(n>0):
        d=n%10
        r=r*10+d
        n=n//10
    if(x==r):
        print("True")
    else:
        print("False")
    