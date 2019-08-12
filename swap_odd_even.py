a=input()
d=list(a)
d[::2],d[1::2]=d[1::2],d[::2]
print(*d,sep="")