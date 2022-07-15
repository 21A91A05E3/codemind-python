s=input()
w=s.split()
for ch in w:
    ma=max(ch)
    mi=min(ch)
    print(ord(ma)-ord(mi),end=" ")