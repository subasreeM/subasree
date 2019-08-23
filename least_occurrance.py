a=int(input())
ar=list(map(int,input().split()))
b=[]
c=[]
e=[]
for i in ar:
	if i not in b:
		c.append(ar.count(i))
		b.append(i)
d=min(c)
for i in ar:
	if(ar.count(i)==d):
		e.append(i)
print(*e[::-1])
		
	
	
	