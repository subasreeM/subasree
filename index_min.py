aa,bb=map(int,input().split())
g=[]
h=[]
a=[int(aa) for aa in input().split() ]
for i in range(0,bb):
    u,v=map(int,input().split())
    for j in range(u-1 ,v):
        h.append(a[j])
    x=sorted(h)
    g.append(min(h))
    del h[:]
for z in range(0,len(g)):
    print(g[z])