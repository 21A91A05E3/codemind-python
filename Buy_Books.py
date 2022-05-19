n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
s1=0
s2=0
for i in range(len(a)):
    s1=s1+a[i]
    s2=s2+b[i]
r=s2-s1
if(r>0):
    print(r)
else:
    print("0")