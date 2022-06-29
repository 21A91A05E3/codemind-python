n=int(input())
l=list(map(int,input().split()))
e=0
o=0
for i in l:
    if i%2==0:
        e=e+i
    else:
        o=o+i
print(abs(e-o))