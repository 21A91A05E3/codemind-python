from math import floor,log2
n=int(input())
l=pow(2,floor(log2(n)))
r=l*2
print(min((n-l),(r-n)))
