aa,bb=input().split()
cost=abs(len(aa)-len(bb))
for i in range(len(aa)):
	if(len(bb)==1 and bb[i] in aa):
		break
	if (aa[i]!=bb[i]):
		cost+=1
print(cost)