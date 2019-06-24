d=input()
f=[]
for i in d:
	if(i.isnumeric()):
		f.append(i)
print(''.join(f))