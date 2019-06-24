d=int(input())
a=list(map(int,input().split()))
for i in range(len(a)):
	if(a[i]>a[i+1]):
		break
print(i)