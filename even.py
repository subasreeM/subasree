a,b = input().split()
start=int(a)
end=int(b)
for i in range(start + 1, end ):
	if (i % 2) == 0:
		print(i, end = " " )