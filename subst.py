a,b=map(int,input().split())
f=set(map(int,input().split()))
d=set(map(int,input().split()))
if d.issubset(f):
	print("YES")
else:
	print("NO")
