n=int(input())
a=list(map(int,input().split()))
for i in range(len(a)):
    b=a[i]
    c=0
    for j in range(len(a)):
        if(a[j]<b):
            c+=1
    print(c,end=' ')