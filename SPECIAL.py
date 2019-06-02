a=input()
count=0
for i in a:
	if i.isnumeric() != True and i.isalpha() != True :
		count+=1
print (count)