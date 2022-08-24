r=int(input())
for i in range (1,r+1):
    for j in range (1, r-i + 1):
        print (end=" ")
    if i == 1 or i == r:
        for j in range (1, r+ 1):
            print ("*",end="")
    else:
        for j in range (1,r+1):
            if (j == 1 or j == r):
                print ("*",end="")
            else:
                print (end=" ")
    print()