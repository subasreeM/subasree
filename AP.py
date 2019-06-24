b,n,m=map(int,input().split())
sum=0
for i in range(1,m+1):
	sum+=b+(m-i)*n
print(sum)