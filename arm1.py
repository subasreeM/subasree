a,b = input().split()
p=int(a)
q=int(b)
for num in range(p + 1, q):
	sum=0
	temp=num
	while(temp>0):
		digit=temp%10
		sum=sum+(digit**3)
		temp=temp//10
	if(num==sum):
		print(num, end = " ")