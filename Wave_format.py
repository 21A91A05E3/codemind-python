n=int(input())
l=list(map(int,input().split()))
l=sorted(l)
l=l[::-1]
for i in range(0,n-1,2):
    j=i+1
    l[i],l[j]=l[j],l[i]
for i in l:
    print(i,end=" ")