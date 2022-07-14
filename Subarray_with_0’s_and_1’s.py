def s(l):
    d = {}
    d[0] = -1
    c= 0
    e= -1
    t= 0
    for i in range(len(l)):
        t += -1 if (l[i] == 0) else 1
        if t in d:
            if c < i - d.get(t):
                c = i - d.get(t)
                e = i
        else:
            d[t] = i
    if e != -1:
        print(e - c + 1, e)
    else:
        print("-1")
n=int(input())
l=list(map(int,input().split()))
s(l)
