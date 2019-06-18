s=int(input())
d=list(map(int,input().split()))
d.sort()
f=d[int(s/2)]
print(f)