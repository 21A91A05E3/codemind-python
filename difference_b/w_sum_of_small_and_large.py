s=input()
w=s.split()
n=len(w)
lr=0
ls=0
for i in w:
    mi=min(i)
    ma=max(i)
    lr=lr+ord(mi)
    ls=ls+ord(ma)
print(ls-lr)
