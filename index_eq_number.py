d=int(input())
f=[int(x) for x in input().split()[:d]]
c=[]
for i in range(0,int(len(f))):
	if(i==f[i]):
		c.append(i)
if(int(len(c))!=0):
	for g in c:
		print(g,end=" ")
else:
	print(-1)
