
n=int(input())
l=list(map(int,input().split()))
r=set(l)
s=sorted(r)
if(len(s)-3>=0):
    print(s[len(s)-3])
else:
    print(max(s))
