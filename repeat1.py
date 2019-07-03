g=int(input())
f=list(map(int,input().split()))
d=[]
for i in range(0,len(f)):
	if(f.count(f[i])>1):
		d.append(f[i])
if(len(d)>=1):
	print(d[0])
else:
	print("unique")
		
