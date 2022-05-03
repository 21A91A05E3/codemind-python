n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if(i<n):
            if(j==1 or j==i):
                print("*",end='')
            else:
                print(" ",end='')
        elif(i==n+1 or j<=n+1):
            print("*",end='')
            
    print( )