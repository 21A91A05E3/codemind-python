def d(n):
    s=0
    p=0
    while n:
        d=n%10
        s=s+(d*(pow(2,p)))
        p+=1
        n=n//10
    print(s)
t=int(input())
for i in range(t):
    n=int(input())
    d(n)