t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    l2=sorted(l)
    c=0
    j=0
    k=-1
    l1=[]
    while(c<len(l2)):
        if l2[k] not in l1:
            l1.append(l2[k])
        if l2[j] not in l1:
            l1.append(l2[j])
        j+=1
        k-=1
        c+=2
    print(*l1)
