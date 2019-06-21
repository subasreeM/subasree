import math
a,b=map(int,input().split())
c=a*b
v=math.sqrt(c)
if int(v+0.5)**2==c:
  print("yes")
else:
  print("no")
