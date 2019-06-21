a,b=map(int,input().split())
m=a*b
for i in range(0,m):
	if(i**2==m):
		print("yes")
		break
else:
	print("no")