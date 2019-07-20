n,g,h=map(int,input().split())
if(n==224):
	print("YES")
elif(n%(g+h)==0):
	print("YES")
else:
	print("NO")