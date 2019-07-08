f=int(input())
s=list(map(int,input().split()))[:f]
for i in s:
	if s.count(i)== 1:
		print(i)