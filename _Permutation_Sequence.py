from itertools import permutations
n,k=map(int,input().split())
s=""
c=0
for j in range(1,n+1):
    s=s+str(j)
for i in range(n,len(s)+1):
    for p in permutations(s,i):
        c+=1
        if c==k:
            print("".join(p),end=" ")
            break