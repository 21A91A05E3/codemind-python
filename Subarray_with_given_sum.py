def subArraySum(arr, n, s):
    curr_sum = arr[0]
    start = 0
    i = 1
    while i <= n:
        while curr_sum > s and start < i-1:
            curr_sum = curr_sum - arr[start]
            start += 1
        if curr_sum == s:
            print (start+1,end=" ")
            print(i)
            return 1
        if i < n:
            curr_sum = curr_sum + arr[i]
        i += 1
    print ("-1")
    return 0
t=int(input())
for i in range(t):
    n,s=map(int,input().split())
    l=list(map(int,input().split()))
    subArraySum(l, n, s)
