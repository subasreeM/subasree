h=int(input())
r=0
for i in range(2,h):
	if(h%i==0):
		r+=1
if(r==0):
	print("yes")
else:
	print("no")