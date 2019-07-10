from itertools import combinations
n,k=map(int,input().split())
g=len(str(n))
a=list(combinations(str(n),g-k))
a=sorted(a)
print("".join(a[0]))
