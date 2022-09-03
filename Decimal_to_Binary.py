def b(n):
    s=''
    while n>1:
        d=n%2
        n=n//2
        s+=str(d)
    s+=str(n)
    return s[::-1]
t=int(input())
for i in range(t):
    n=int(input())
    print(b(n))