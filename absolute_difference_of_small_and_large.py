s=input()
w=s.split()
n=len(w)
for i in w:
    mi=min(i)
    ma=max(i)
    r=abs(ord(mi)-ord(ma))
    print(r,end=" ")
