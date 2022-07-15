n=int(input())
l=list(map(int,input().split()))
s=0
for i in l:
    s=s+i
r=s/n
print('%.2f'%r)
