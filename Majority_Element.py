n=int(input())
a=list(map(int,input().split()))
for i in range (n):
    c=1
    for j in range(n):
        if(a[i]>0):
            if(a[i]==a[j] and i!=j):
                c+=1
                a[j]=-1
    if(c>n//2):
        print(a[i])