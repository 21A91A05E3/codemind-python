n=int(input())
for i in range(n):
    for j in range(n):
        if(i==j or j==n-1-i):
            print('x',end='')
        else:
            print('0',end='')
    print( )