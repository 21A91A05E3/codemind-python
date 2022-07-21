n=int(input())
k=n
s=(2*n)-1
l=[[0 for i in range(s)] for j in range(s)]
for i in range(n):
    for j in range(i,s-i):
        l[i][j]=k
        l[s-i-1][j]=k
        l[j][i]=k
        l[j][s-i-1]=k
    k-=1
for i in range(s):
    for j in range(s):
        print(l[i][j],end=" ")
    print()