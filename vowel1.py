g=input()
l=len(g)
c=0
for i in range(l):
	if(g[i] in('a','e','i','o','u')):
		c+=1
if(c>0):
	print("yes")
else:
	print("no")