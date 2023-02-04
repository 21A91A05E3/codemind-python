n=int(input())
l1=[list(map(int,input().split())) for i in range(n)]
l2=[list(map(int,input().split())) for i in range(n)]
l=[]
for i in range(n):
    r=[]
    for j in range(n):
        r.append(abs(l1[i][j]-l2[i][j]))
    l.append(r)
for i in range(n):
    for j in range(n):
        if j!=n-1:
            print(l[i][j],end=" ")
        else:
            print(l[i][j])

            

