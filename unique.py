d=int(input())
f=list(map(int,input().split()))
for i in range(0,len(f)):
	if(f.count(f[i])==1):
		print(f[i])
	