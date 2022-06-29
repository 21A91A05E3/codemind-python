import math
def is_prime(n):
    return n > 1 and all(n % d for d in range(2, int(math.sqrt(n)) + 1))
def NextprimePalindrome(N):
    for k in range(1, 10**6):
        s = str(k)
        x = int(s + s[-2::-1]) 
        if x >N and is_prime(x):
            return x
        s = str(k)
        x = int(s + s[-1::-1])  
        if x > N and is_prime(x):
            return x
N =int(input())
print(NextprimePalindrome(N))