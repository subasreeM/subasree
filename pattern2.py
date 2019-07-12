 n=int(input())
for i in range(0,n):
	for j in range(0,n-i-1):
		print(" ",end="")
	for k in range(0,i):
		print(k+1,end=" ")
	if(i%2==0):
		print(i%2+1)
	else:
		print(i%2)
for i in range(n-2,-1,-1):
	for j in range(n-i-2,-1,-1):
		print(" ",end="")
	for k in range(0,i):
		print(k+1,end=" ")
	if(i%2==0):
		print(i%2+1)
	else:
		print(i%2)
	