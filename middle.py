d=list(input())
if(len(d)%2==0):
	d[int(len(d)/2)]="*"
	d[int(len(d)/2)-1]="*"
else:
	d[int(len(d)/2)]="*"
for i in range(0,len(d)):
	print(d[i],end="")
