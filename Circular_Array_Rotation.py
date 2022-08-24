n,k,q=map(int,input().split())
l=list(map(int,input().split()))
w=[]
for i in range(q):
    a=int(input())
    w.append(a)
for i in w:
    print(l[(n-k+i)%n])
    