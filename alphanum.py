a=input()
d=0
e=0
for i in a:
	if i.isnumeric():
		d=d+1
	elif i.isalpha():
		e=e+1
if(d>=1 and e>=1):
	print("yes")
else:
	print("no")
