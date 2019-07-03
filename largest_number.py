g=int(input())
f=list(map(int,input().split()))
f.sort(reverse=True)
h=0
for i in range(0,len(f)):
	h=(h*10)+f[i]
print(h)