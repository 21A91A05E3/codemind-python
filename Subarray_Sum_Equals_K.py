def s(nums,k):
    d={}
    c=0
    a=0
    for i in nums:
        a+=i
        if a==k:
            c+= 1
        if a-k in d:
            c+= d[a-k]
        if a in d:
            d[a] += 1
        else:
            d[a] = 1
    print(c)
a,b=map(int,input().split())
l=list(map(int,input().split()))
s(l,b)