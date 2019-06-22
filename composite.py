d=int(input())
if(d>0):
	for i in range(2,d):
		if(d%i==0):
			print("yes")
			break
	else:
		print("no")
else:
	print("yes")