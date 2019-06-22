d,e=map(int,input().split())
f=list(map(int,input().split()))
g=[]
for i in range(0,len(f)):
	if(f[i]%2!=0):
		g.append(f[i])
print(g[e-1])