a,b = input().split()
start=int(a)
end=int(b)
for num in range(start + 1, end ):
	if num > 1:
		for i in range(2,num):
			if (num % i) == 0:
				break
		else:
			print(num)
		