f=int(input())
d=list(map(int,input().split()))[:f]
for i in range(0,f-2):
	for j in range(i+1,f-1):
		for k in range(j+1,f):
			if(d[i]+d[j]==d[k]):
				print(d[i],d[j],d[k])
		