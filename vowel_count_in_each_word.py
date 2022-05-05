s=input()
w=s.split()
for i in w:
    v=sum(letter in 'aeiou' for letter in i.lower())
    print(v,end=' ')