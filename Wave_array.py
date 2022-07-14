def isWaveArray(arr , n):
    result = True
    if (arr[1] > arr[0] and arr[1] > arr[2]):
        for i in range(1, n - 1, 2):
            if (arr[i] > arr[i - 1] and
                arr[i] > arr[i + 1]):
                result = True
            else :
                result = False
                break
        if (result == True and n % 2 == 0):
            if (arr[n - 1] <= arr[n - 2]) :
                result = False
    elif (arr[1] < arr[0] and
          arr[1] < arr[2]) :
        for i in range(1, n - 1, 2) :
            if (arr[i] < arr[i - 1] and
                arr[i] < arr[i + 1]):
                result = True
            else :
                result = False
                break
        if (result == True and n % 2 == 0) :
            if (arr[n - 1] >= arr[n - 2]) :
                result = False
    return result
n=int(input())
l=list(map(int,input().split()))
r=isWaveArray(l,n)
if(r==True):
    print("yes")
else:
    print("no")