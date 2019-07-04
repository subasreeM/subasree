d=int(input())
arr=list(map(int,input().split()))
c=0
for i in range(0,d-2):
	for j in range(1,d-1):
		for k in range(2,d):
			if((arr[i] < arr[j]) and (arr[j] < arr[k])):
				c+=1
print(c)
