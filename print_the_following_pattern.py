n=int(input())
k=ord("A")
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(chr(k+i-1),end=' ')
    print( )
        