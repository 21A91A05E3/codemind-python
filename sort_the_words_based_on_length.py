s=input()
w=s.split()
w.sort()
w.sort(key=len)
for i in w:
    print(i,end=" ")