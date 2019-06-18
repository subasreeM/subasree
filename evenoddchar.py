d=str(input())
s=[]
t=[]
for i in range(0,len(d)):
	if(i%2==0):
		s.append(d[i])
	else:
		t.append(d[i])
print("".join(s),"".join(t))