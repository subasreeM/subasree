k=int(input())
f=list(map(int,input().split()))
p=[]
for i in range(len(f)):
	if f.count(f[i])>1:
		if f[i] not in p:
			p.append(f[i])
p.sort()
if(len(p)==0):
	print("unique")
else:
	print(" ".join(str(j) for j in p))