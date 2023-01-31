t=int(input())
for i in range(t):
    n=input()
    n=int(n,16)
    n=bin(n)
    n=n[2:]
    l=len(n)
    if l%4:
        for j in range(0,4-(l%4)):
            n="0"+n
    print(n)
