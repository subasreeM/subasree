f=int(input())
d=list(map(int,input().split()))[:f]
for i in range(0,f):
	if(i % 2 == 0 and d[i] % 2 == 1):
		print(d[i],end=" ")
	if(i % 2 == 1 and d[i] % 2 == 0):
		print(d[i],end=" ")
	