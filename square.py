import math
d,e=map(int,input().split())
c=d*e
u=math.sqrt(c)
if int(u+0.5)**2==c:
  print("yes")
else:
  print("no")
