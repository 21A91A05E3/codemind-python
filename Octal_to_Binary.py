t=int(input())
for i in range(t):
    n=input()
    n=int(n,8)
    n=bin(n)
    n=n[2:]
    print(n)
