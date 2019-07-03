g=int(input())
f=list(map(int,input().split()))
d=[]
for i in range(0,len(f)):
	if(f.count(f[i])>1):
		d.append(f[i])
if(len(f)>=1):
	print(f[0])
else:
	print("unique")
		