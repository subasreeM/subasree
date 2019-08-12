d=input()
d.lower()
s=list(d)
for i in range(0,len(s)):
	if(s[i]==" "):
		s[i+1]=s[i+1].upper()
print(*s,sep="")