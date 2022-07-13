from itertools import permutations
s=input()
for p in permutations(s,len(s)):
    print("".join(p))