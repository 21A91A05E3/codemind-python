def c(n):
    if n<=2:
        return n
    a=1
    b=1
    c=2
    r=0
    for i in range(3,n+1):
        r=a+b+c
        a=b
        b=c
        c=r
    return r
n = int(input())
print(c(n))