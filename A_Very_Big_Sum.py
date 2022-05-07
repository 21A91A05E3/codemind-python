n=int(input())
sum=0
a=list(map(int,input().split()))
for i in range(len(a)):
    sum=sum+a[i]
print(sum)