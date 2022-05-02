s=input()
w=s.split()
rw=[ ]
for i in w:
    rw.append(i[::-1])
print(" ".join(rw))