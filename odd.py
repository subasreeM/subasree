a,b = input().split()
n=int(a)
end=int(b)
for i in range(n + 1 , end ):
	if i % 2 != 0:
		print(i, end = " ")
