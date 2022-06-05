s=input()
w=s.split()
w.reverse()
l=[i[::-1] for i in w]
print(" ".join(l))