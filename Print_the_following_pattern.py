n=int(input())
for i in range(n):
    for j in range(n-i):
        print(j+i+1,end=' ')
    print( )