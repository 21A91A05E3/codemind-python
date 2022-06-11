n=input()
l=list(map(int,input().split()))
c=0
m=9999
for i in l:
    if m>i:
        m=i
for i in range(m,0,-1):
    c=0
    for j in range(len(l)):
        if(l[j]%i!=0):
            c=1
            break
    if c==0:
        print(i)
        break