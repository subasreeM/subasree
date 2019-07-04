a,b=map(int,input().split())
g=[]
h=[]
f=list(map(int,input().split()))[:a]
for i in range(0,b):
    u,v=map(int,input().split())
    for j in range(u-1 ,v):
        g.append(f[j])
    k=sum(g)
    h.append(k)
print(h[0])
for x in range(1,len(h)):
    print(h[x]- h[x- 1])